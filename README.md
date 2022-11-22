# Projeto Computer Vision Full - BMSrecognition (Building Material Store recognition -> Reconhecimento para Loja de Material de Construção)

Projeto desenvolvido para a Disciplina de Computação Gráfica | Atitus 2022

# Professor
Marcos R. Santos

# Integrante
Arthur Rebonato - RA 1120468

# Descrição
Projeto feito com IA para detectar um objeto, que nesse projeto foi caminhões, para localizar e marcar o horário que saiu e entrou no pátio da loja. Além disso, possui reconhecimento facial para realizar o horário de chegada e saída dos funcionários no trabalho.

# Propósito
Facilitar e modernizar os registros de entrada e saída dos funcionários no horário de trabalho através da reconhecimento facial. Além, de tirar fotos com a data e horário das idas e vindas dos caminhões nas entregas, com o intuito de fazer o registro de entregas.

# Libs Utilizadas
python = 3.10.6<br>
opencv-python = 4.6.0.66<br>
numpy = 1.23.4<br>
cmake = 3.24.3<br>
dlib = 19.24.0<br>
click = 8.1.3<br>
colorama = 0.4.6<br>
face-recognition = 1.3.0<br>
face-recognition-models = 0.3.0<br>
Pillow = 9.3.0<br>

# Link para as Imagens (positivas e negativas) e Vídeo Teste 
https://drive.google.com/drive/folders/1Vk5kwXV0W6ebzzGWI-g4IdueK-bAzpNN?fbclid=IwAR2p1r_i4fvD4o52Jordumg1n47hBanag6VTamEtO8CApNagB2a8h_e5hkQ

# Requisitos das Tarefas

## Técnicas de Processamento de Imagens
<div align="center">
<img src="https://user-images.githubusercontent.com/67520671/203188142-12406340-68e4-410a-bb39-fef62305b12f.png" width="400px">
<img src="https://user-images.githubusercontent.com/67520671/203188131-8e9d52c6-ce5d-436b-aa03-60cc08dd1171.png" width="400px">
<img src="https://user-images.githubusercontent.com/67520671/203188126-055600c8-bc11-42e3-9c46-109bbab467c6.png" width="400px">
<img src="https://user-images.githubusercontent.com/67520671/203188149-aab48722-54b4-43b6-bbbc-3b764ae46f46.png" width="400px">
</div>

## HaarCascade Truck

## - CreateSamples
<div align="center">
<img src="https://user-images.githubusercontent.com/67520671/203188847-64b41fd1-d134-436b-99bc-f286e395c6b6.png" width="400px">
</div>

## - Training
<div align="center">
<img src="https://user-images.githubusercontent.com/67520671/203188868-c15e3745-eb19-429e-8544-e5ceed8153b2.png" width="400px"><br>
<img src="https://user-images.githubusercontent.com/67520671/203188862-462545d9-79e5-4831-aa83-7e11ffead9dd.png" width="400px"><br>
<img src="https://user-images.githubusercontent.com/67520671/203188866-83df7b38-c550-47f9-bb0b-0347f71f0196.png" width="400px">
</div>

## - Arquivos .xml
<div align="center">
<img src="https://user-images.githubusercontent.com/67520671/203188881-27c31d84-6eee-4c35-9e2a-128a62ffb930.png" width="400px"><br>
<img src="https://user-images.githubusercontent.com/67520671/203188882-5ca1f603-a488-48f7-9dab-2eae0434f973.png" width="400px">
</div>

## Log -> txt e imagem

## - Face
<div align="center">
<img src="https://user-images.githubusercontent.com/67520671/203190579-4f8dbbfb-a453-4a98-9494-0e032ed99c0e.png" width="400px">
<img src="https://user-images.githubusercontent.com/67520671/203190593-ae2dbe10-34ff-405c-bceb-a5bd128e4773.png" width="400px">
</div>

## - Truck
<div align="center">
<img src="https://user-images.githubusercontent.com/67520671/203190657-4552efce-b296-41ea-bb17-b973fd65cda1.png" width="400px">
<img src="https://user-images.githubusercontent.com/67520671/203190667-98262408-ff4b-4131-a6ac-8a9b386a584c.png" width="400px">
</div>

## Reconhecimento Facial
<div align="center">
<img src="https://user-images.githubusercontent.com/67520671/203191114-23bf276d-0209-44ad-baab-fa8d8cd1a055.png" width="400px">
<img src="https://user-images.githubusercontent.com/67520671/203191128-ccc4ed21-fe75-4122-937a-8e7b7d6b1d69.png" width="400px"><br>
<img src="https://user-images.githubusercontent.com/67520671/203191136-64335760-3b4b-4144-bf53-cf609a97018d.jpg" width="400px">
</div>

## Técnicas de Binarização e Detecção de Bordas
<div align="center">
<img src="https://user-images.githubusercontent.com/67520671/203191372-2f43a092-b09c-45b8-8b13-42b6867ce0be.png" width="400px">
</div>

## Seleção de Objetos por Cores
<div align="center">
<img src="https://user-images.githubusercontent.com/67520671/203191598-a68accb3-e720-40e7-8785-0a370ef1c76f.png" width="400px">
</div>
