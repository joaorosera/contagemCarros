import cv2
import numpy as np

# Vídeo da atividade
video = cv2.VideoCapture("carros-passando.mp4")

# Contador de carros
contador = 0

# Controla se a área de contagem já está livre para contar outro carro
liberado = True

# Subtrator de fundo: ajuda a detectar o que está se movimentando no vídeo
subtrator = cv2.createBackgroundSubtractorMOG2(
    history=80,
    varThreshold=40,
    detectShadows=True
)

while True:
    ret, img = video.read()

    # Quando acabar o vídeo, sai do loop
    if not ret:
        break

    # Ajusta o tamanho da imagem para trabalhar com coordenadas fixas
    img = cv2.resize(img, (1100, 620))

    # Região de contagem: uma faixa vertical na rua
    # Se precisar ajustar para outro vídeo, altere esses valores
    x, y, w, h = 550, 330, 60, 210

    # Aplica uma leve suavização para reduzir ruídos
    imgBlur = cv2.GaussianBlur(img, (5, 5), 0)

    # Cria uma máscara com os objetos em movimento
    imgSub = subtrator.apply(imgBlur)

    # Remove sombras e deixa apenas partes mais brancas da máscara
    _, imgTh = cv2.threshold(imgSub, 200, 255, cv2.THRESH_BINARY)

    # Dilata a imagem para juntar melhor as partes do carro
    kernel = np.ones((5, 5), np.uint8)
    imgDil = cv2.dilate(imgTh, kernel, iterations=2)

    # Recorta apenas a região de contagem
    recorte = imgDil[y:y+h, x:x+w]

    # Conta quantos pixels brancos existem na faixa
    brancos = cv2.countNonZero(recorte)

    # Valor mínimo para considerar que tem um carro passando na faixa
    limite = 1200

    # Se passou do limite e a faixa estava liberada, conta 1 carro
    if brancos > limite and liberado:
        contador += 1
        liberado = False

    # Quando a faixa volta a ficar vazia, libera para contar o próximo carro
    if brancos < limite:
        liberado = True

    # Cor da faixa:
    # Verde = carro passando / ocupada
    # Rosa = livre
    if liberado:
        cor = (255, 0, 255)
    else:
        cor = (0, 255, 0)

    # Desenha a área de contagem no vídeo original
    cv2.rectangle(img, (x, y), (x + w, y + h), cor, 4)

    # Desenha a área de contagem também na imagem tratada
    cv2.rectangle(imgDil, (x, y), (x + w, y + h), (255, 255, 255), 4)

    # Mostra informações na tela
    cv2.putText(img, f"Pixels: {brancos}", (x - 120, y - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    cv2.rectangle(img, (20, 20), (270, 100), (255, 255, 255), -1)
    cv2.putText(img, f"Carros: {contador}", (35, 75),
                cv2.FONT_HERSHEY_SIMPLEX, 1.4, (255, 0, 0), 4)

    print("Carros:", contador)

    cv2.imshow("Video original", img)
    cv2.imshow("Mascara", imgDil)

    # ESC fecha o vídeo
    if cv2.waitKey(20) == 27:
        break

video.release()
cv2.destroyAllWindows()
