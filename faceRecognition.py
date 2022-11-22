import face_recognition
import cv2
import numpy as np
import os
import glob
from datetime import datetime
import time

# Função para verificar e se registrar na entrada e saida de serviço
def verificaRegistro(nome, texto):
    # Pega o horário atual e formata a data e hora
    data_hora = datetime.now()
    data_atual = data_hora.strftime('%d/%m/%Y %H:%M')

    # Verifica se o rosto é de alguem cadastrado
    if nome != "" and nome != "desconhecido":
        # Texto que vai ser inserido no .txt da entrada e saida com o dia e hora
        textoRegistro = nome + texto + data_atual + "\n"

        # Váriavel para verificar se ja foi inserido o texto
        verifica = False
            
        # Abre o arquivo registro.txt no modo leitura
        with open("registro.txt", "r") as arquivo:
            # Percorre linha por linha do arquivo
            for linha in arquivo:
                # Se o texto estiver no arquivo muda a variável para True
                if textoRegistro == linha:
                    verifica = True

        # Se o texto não estiver no arquivo realiza a escrita
        if verifica == False:
            # Abre o arquivo no modo escrita
            with open("registro.txt","a") as f:
                # Escreve o texto no arquivo
                f.write(textoRegistro)
                verifica = True
                # Inserido um texto no vídeo para indicar que o registro foi feito
                cv2.putText(frame, "Registrado com Sucesso!", (100, 50),
                    font, 1, (0, 255, 0), 2)
                time.sleep(6)

# Função para desenhar o contorno das cores verde e vermelho e executar uma ação
def contornoCor(nome, mask, cor):
    # Encontra os contornos da imagem
    contornos, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Percorre cada contorno
    for contorno in contornos:
        # Captura a área do contorno
        area = cv2.contourArea(contorno)

        # Se a área for maior que 1500 desenha o contorno convexo e executa uma ação para cada cor
        if area > 1500:
            novoContorno = cv2.convexHull(contorno)
            cv2.drawContours(frame, [novoContorno], 0, cor, 3)

            #Se a cor for verde faz o registro que entrou em serviço
            if cor == (0, 255, 0):
                verificaRegistro(nome, " entrou em servico - ")
            #Se a cor for vermelho faz o registro que saiu de serviço
            elif cor == (0, 0, 255):
                verificaRegistro(nome, " saiu de servico - ")

# lista dos nomes e codificações das faces
faces_encodings = []
faces_names = []

# Retorna o diretório atual e vai para a pasta faces
cur_direc = os.getcwd()
path = os.path.join(cur_direc, 'faces/')

# Lista com os arquivos faces .jpg
list_of_files = []
list_of_files = [f for f in glob.glob(path+'*.jpg')]

# Pega o tamanho da lista e faz uma copia dos nomes
number_files = len(list_of_files)
names = list_of_files.copy()
    
#HSV do verde com baixo e alto
lowerGreen = np.array([50, 90, 175])
upperGreen = np.array([65, 255, 255])

#HSV do vermelho com baixo e alto
lowerRed = np.array([170, 90, 150])
upperRed = np.array([179, 255, 255])

# Faz um loop da quantidade de arquivos
for i in range(number_files):
    # Carrega um arquivo e retorna a codificação de face
    presets = face_recognition.load_image_file(list_of_files[i])
    encoding = face_recognition.face_encodings(presets)[0]

    # Adiciona a codificação na lista
    faces_encodings.append(encoding)

    # Pega os nomes das pessoas e adiciona na lista de nome das faces
    nome = names[i].replace(cur_direc+"\\faces\\", "")
    nome = nome.replace(".jpg", "")
    names[i] = nome
    faces_names.append(names[i])

# lista da localização por matrizes, nomes e codificações das faces
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

# Abre o dispositivo de captura
video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    # Lê a câmera
    ret, frame = video_capture.read()

    # Inverte horizontalmente a câmera
    frame = cv2.flip(frame, 1)
    name = ""

    # Redimensiona a imagem em 1/4
    rgb_small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    if process_this_frame:
        # Retorna a matriz de caixas delimitadoras e codificação de face
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(
            rgb_small_frame, face_locations)
        face_names = []

        # Pega cada codificação de face
        for face_encoding in face_encodings:
            # Faz a comparação de face com a lista e se não bater é chamado de Desconhecido
            matches = face_recognition.compare_faces(
                faces_encodings, face_encoding)
            name = "Desconhecido"

            # Faz a comparação pela codificação e obtem uma distancia para cada face
            face_distances = face_recognition.face_distance(
                faces_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)

            # Se bater uma face pega o nome e adiciona na lista de nomes de faces
            if matches[best_match_index]:
                name = faces_names[best_match_index]
            face_names.append(name)
    # Faz um loop com as localizações e nomes das faces
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Volta o tamanho para o original
        top = int(top*4)
        right = int(right*4)
        bottom = int(bottom * 4)
        left = int(left * 4)
        # Desenha o contorno retangulo na face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35),
                      (right, bottom), (0, 0, 255), cv2.FILLED)
        # Escreve o nome no vídeo
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6),
                    font, 0.5, (255, 255, 255), 1)
    # Converte para HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Construção das mascara para todas as cores
    maskGreen = cv2.inRange(hsv, lowerGreen, upperGreen)
    maskRed = cv2.inRange(hsv, lowerRed, upperRed)

    #Chama a função passando o nome da pessoa, a mascara de uma cor com sua cor em BGR para o contorno
    contornoCor(name, maskGreen, (0, 255, 0))
    contornoCor(name, maskRed, (0, 0, 255))

    # Exibe o vídeo
    cv2.imshow('Video', frame)

    # Aguarda em milissegundos uma tecla ser pressionada e ao apertar o Esc fecha
    k = cv2.waitKey(10)
    if k == 27:
        break

# Fecha a janela com a imagem aberta
cv2.destroyAllWindows()

# Finaliza a conexão com a câmera
video_capture.release()
