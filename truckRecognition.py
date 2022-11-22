import cv2
import numpy as np
import os
from datetime import datetime, timedelta

# Abre o vídeo
camera = cv2.VideoCapture("truckChegada.mp4")

# Lê o modelo pré-treinados dos caminhões
cascade = cv2.CascadeClassifier("treinamento/cascade.xml")

# Lista para adicionar outros nomes de arquivos, com objetivo de evitar colocar mais imagens em pouco tempo
possiveisNomes = []

while True:
    # Lê a câmera
    _, imagemC = camera.read()

    # Converte a imagem para cinza
    gray = cv2.cvtColor(imagemC, cv2.COLOR_BGR2GRAY)

    # Suaviza a imagem, para tirar ruídos
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Aplica um limiar simples, usado para criar imagens binárias
    limiar = 134
    _, bin = cv2.threshold(blur, limiar, 255, cv2.THRESH_BINARY)

    # Dilata a imagem, para aumentar o tamanho do objeto
    dilated = cv2.dilate(bin, np.ones((3,3)))

    # Constroi o elemento estruturante circular, seguida uma operaçao de fechamento
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
    closing = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)

    # Detecta objetos de diferentes tamanhos na imagem
    objetos = cascade.detectMultiScale(closing, 1.13, 7)

    # Pega o horário e data atual, formata e escreve no vídeo
    font = cv2.FONT_HERSHEY_DUPLEX
    data_hora = datetime.now()
    data_atual = data_hora.strftime('%d/%m/%Y %H:%M')

    cv2.putText(imagemC, data_atual, (20, 50),
                font, 1.5, (255, 255, 255), 2)

    # Faz um loop pegando as coordenadas e altura/largura dos objetos
    for (x, y, w, h) in objetos:
        # Se largura * altura for maior que 120000
        if (w * h) > 120000:
            # Retorna o diretório atual e vai para a pasta entregas
            cur_direc = os.getcwd()
            path = os.path.join(cur_direc, 'entregas/')

            # Declara o nome da imagem, pegando a data formatada e adicionando .jpg
            nomeImg = data_hora.strftime("%d-%m-%Y %H'%M") + ".jpg"

            # Se o nome não estiver na lista possiveisnomes, salva a imagem e adiciona na lista
            if (nomeImg in possiveisNomes) == False:
                cv2.imwrite(path + nomeImg, imagemC)
                possiveisNomes.append(nomeImg)
            
            # Faz um loop adicionando na lista possiveisnomes, os nomes mudam apenas poucos minutos
            for i in range(1,4):
                possivelData = data_hora + timedelta(minutes=i)
                possivelNomeImg = possivelData.strftime("%d-%m-%Y %H'%M") + ".jpg"
                possiveisNomes.append(possivelNomeImg)

            # Desenha o contorno no objeto
            cv2.rectangle(imagemC, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # Pega o tamanho da imagem e redimensiona para ficar menor
    height, width, bpp = np.shape(imagemC)
    resizeMin = cv2.resize(imagemC, (int(width/1.7), int(height/1.7) ) ,interpolation=cv2.INTER_CUBIC )

    # Aguarda em milissegundos uma tecla ser pressionada e ao apertar o Esc fecha
    k = cv2.waitKey(1)
    if k == 27:
        break

    # Exibe o vídeo
    cv2.imshow("Truck", resizeMin)

# Fecha a janela com a imagem aberta
cv2.destroyAllWindows()

# Finaliza a conexão com a câmera
camera.release()
