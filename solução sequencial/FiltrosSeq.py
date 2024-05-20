from PIL import Image
import tkinter as tk
from tkinter import filedialog
import os
import math
import time

def filtro_mediana(img):
    width, height = img.size
    newimg = Image.new("RGB", (width, height), "white")
    for i in range(1, width - 1):
        for j in range(1, height - 1):
            # Coletando os valores dos pixels ao redor do pixel atual (máscara 3x3)
            r_values = [
                img.getpixel((i - 1, j - 1))[0], img.getpixel((i - 1, j))[0], img.getpixel((i - 1, j + 1))[0],
                img.getpixel((i, j - 1))[0], img.getpixel((i, j))[0], img.getpixel((i, j + 1))[0],
                img.getpixel((i + 1, j - 1))[0], img.getpixel((i + 1, j))[0], img.getpixel((i + 1, j + 1))[0]
            ]
            g_values = [
                img.getpixel((i - 1, j - 1))[1], img.getpixel((i - 1, j))[1], img.getpixel((i - 1, j + 1))[1],
                img.getpixel((i, j - 1))[1], img.getpixel((i, j))[1], img.getpixel((i, j + 1))[1],
                img.getpixel((i + 1, j - 1))[1], img.getpixel((i + 1, j))[1], img.getpixel((i + 1, j + 1))[1]
            ]
            b_values = [
                img.getpixel((i - 1, j - 1))[2], img.getpixel((i - 1, j))[2], img.getpixel((i - 1, j + 1))[2],
                img.getpixel((i, j - 1))[2], img.getpixel((i, j))[2], img.getpixel((i, j + 1))[2],
                img.getpixel((i + 1, j - 1))[2], img.getpixel((i + 1, j))[2], img.getpixel((i + 1, j + 1))[2]
            ]

            # Ordenando os valores para encontrar o valor mediano para cada canal
            r_values.sort()
            g_values.sort()
            b_values.sort()

            # Atribuindo os valores medianos ao pixel da nova imagem
            newimg.putpixel((i, j), (r_values[4], g_values[4], b_values[4]))
    return newimg

def filtro_sobel(img):
    width, height = img.size
    newimg = Image.new("RGB", (width, height), "white")
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
    return newimg

def selecionar_imagem():
    root = tk.Tk()
    root.withdraw()  # Ocultar a janela principal

    # Abrir o gerenciador de arquivos do sistema operacional para selecionar a imagem
    path = filedialog.askopenfilename(filetypes=[("Imagens", "*.jpg;*.jpeg;*.png;*.gif;*.bmp")])
    return path

def main():
    # Solicitar ao usuário que selecione a imagem
    print("Por favor, selecione a imagem de entrada:")
    path = selecionar_imagem()

    # Verificar se o usuário cancelou a seleção da imagem
    if not path:
        print("Nenhuma imagem selecionada. Encerrando o programa.")
        return

    # Carregar a imagem com ruído
    img_noise = Image.open(path).convert("RGB")
    
    # Medindo o tempo de execução do filtro mediana
    start_mediana = time.time()
    img_mediana = filtro_mediana(img_noise)
    end_mediana = time.time()
    print("Tempo de execução do filtro mediana:", end_mediana - start_mediana, "segundos")

    # Medindo o tempo de execução do filtro Sobel
    start_sobel = time.time()
    img_sobel = filtro_sobel(img_mediana)
    end_sobel = time.time()
    print("Tempo de execução do filtro Sobel:", end_sobel - start_sobel, "segundos")

    # Calculando e imprimindo o tempo total de execução
    tempo_total = end_sobel - start_mediana
    print("Tempo total de execução:", tempo_total, "segundos")

    # Salvando a imagem resultante com nome baseado no nome da imagem de entrada
    img_sobel.save("final_" + os.path.basename(path))

if __name__ == "__main__":
    main()