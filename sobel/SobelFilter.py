from PIL import Image
import math

# Caminho para a imagem
path = "Ballons_noiseless.jpg"
# Abertura da imagem
img = Image.open(path)
# Obtendo as dimensões da imagem
width, height = img.size
# Criando uma nova imagem para armazenar o resultado
newimg = Image.new("RGB", (width, height), "white")

# Aplicando o filtro Sobel
for x in range(1, width-1):
    for y in range(1, height-1):
        # Inicializando Gx e Gy
        Gx = 0
        Gy = 0

        # Coletando os valores de intensidade dos pixels ao redor
        # Cálculo para o pixel superior esquerdo
        p = img.getpixel((x-1, y-1))
        intensity = sum(p)
        Gx += -intensity
        Gy += -intensity

        # Coluna à esquerda
        p = img.getpixel((x-1, y))
        intensity = sum(p)
        Gx += -2 * intensity

        p = img.getpixel((x-1, y+1))
        intensity = sum(p)
        Gx += -intensity
        Gy += intensity

        # Pixel superior
        p = img.getpixel((x, y-1))
        intensity = sum(p)
        Gy += -2 * intensity

        # Pixel inferior
        p = img.getpixel((x, y+1))
        intensity = sum(p)
        Gy += 2 * intensity

        # Coluna à direita
        p = img.getpixel((x+1, y-1))
        intensity = sum(p)
        Gx += intensity
        Gy += -intensity

        p = img.getpixel((x+1, y))
        intensity = sum(p)
        Gx += 2 * intensity

        p = img.getpixel((x+1, y+1))
        intensity = sum(p)
        Gx += intensity
        Gy += intensity

        # Calculando o comprimento do gradiente (Teorema de Pitágoras)
        length = math.sqrt((Gx * Gx) + (Gy * Gy))

        # Normalizando o comprimento do gradiente para o intervalo 0 a 255
        length = int(length / 4328 * 255)

        # Definindo o pixel na nova imagem com o valor normalizado
        newimg.putpixel((x, y), (length, length, length))

# Salvando a nova imagem com o filtro Sobel aplicado
newimg.save("sobel_filtered.jpg")