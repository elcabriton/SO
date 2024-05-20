from PIL import Image

# Caminho para a imagem com ruído
path = "ballons.jpg"
# Abrindo a imagem
img = Image.open(path)
# Convertendo a imagem para o modo RGB, caso não esteja
img = img.convert("RGB")
# Obtendo as dimensões da imagem
width, height = img.size
# Criando uma nova imagem para armazenar o resultado
newimg = Image.new("RGB", (width, height), "white")

# Aplicando o filtro mediana separadamente para cada canal (R, G, B)
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

# Salvando a nova imagem com o filtro mediana aplicado
newimg.save("v2_filtered_image.jpg")
