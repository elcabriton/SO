from PIL import Image

# Caminho para a imagem com ruído
path = "ballons.jpg"
# Abrindo a imagem
img = Image.open(path)
# Obtendo as dimensões da imagem
width, height = img.size
# Criando uma nova imagem para armazenar o resultado
newimg = Image.new("RGB", (width, height), "white")

# Lista para armazenar os valores dos pixels na máscara 3x3
members = [(0, 0, 0)] * 9

# Aplicando o filtro mediana
for i in range(1, width - 1):
    for j in range(1, height - 1):
        # Coletando os valores dos pixels ao redor do pixel atual (máscara 3x3)
        members[0] = img.getpixel((i - 1, j - 1))
        members[1] = img.getpixel((i - 1, j))
        members[2] = img.getpixel((i - 1, j + 1))
        members[3] = img.getpixel((i, j - 1))
        members[4] = img.getpixel((i, j))
        members[5] = img.getpixel((i, j + 1))
        members[6] = img.getpixel((i + 1, j - 1))
        members[7] = img.getpixel((i + 1, j))
        members[8] = img.getpixel((i + 1, j + 1))
        
        # Ordenando os pixels para encontrar o valor mediano
        members.sort()
        
        # Atribuindo o valor mediano ao pixel da nova imagem
        newimg.putpixel((i, j), members[4])

# Salvando a nova imagem com o filtro mediana aplicado
newimg.save("filtered_image.jpg")