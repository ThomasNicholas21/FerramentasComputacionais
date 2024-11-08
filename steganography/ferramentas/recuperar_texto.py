from PIL import Image

T = '1111111111111110'

def extrair_texto(image_path):
    imagem = Image.open(image_path)

    if imagem.mode != "RGB":
        imagem = imagem.convert("RGB")

    comprimento, altura = imagem.size
    binario_texto = ""
    T_len = len(T)  # O tamanho do marcador de término T

    # Percorre os pixels da imagem para coletar o texto binário
    for y in range(altura):
        for x in range(comprimento):
            r, g, b = imagem.getpixel((x, y))
            binario_texto += str(r & 1)  # Extrai o bit menos significativo do valor de R

    # Remove o marcador T, que está no final do texto embutido
    texto_binario = binario_texto[:-T_len]  # Remove os bits correspondentes ao marcador T
    texto = ''

    # Converte os bits binários em caracteres
    for i in range(0, len(texto_binario), 8):
        byte = texto_binario[i:i+8]
        texto += chr(int(byte, 2))

    return texto