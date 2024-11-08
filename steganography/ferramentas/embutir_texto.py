from PIL import Image

T = '1111111111111110'

def texto_embutido(image_path, text, output_path):
    imagem = Image.open(image_path)

    if imagem.mode != "RGB":
        imagem = imagem.convert("RGB")

    encoded = imagem.copy()
    comprimento, altura = imagem.size
    index = 0
    
    texto_binario = ''.join([format(ord(char), '08b') for char in text]) + T  

    for y in range(altura):
        for x in range(comprimento):
            if index < len(texto_binario):
                r, g, b = imagem.getpixel((x, y))
                r = (r & ~1) | int(texto_binario[index])
                encoded.putpixel((x, y), (r, g, b))
                index += 1
            else:
                break
    
    print(texto_binario)
    encoded.save(output_path)
    print("Texto embutido com sucesso na imagem.")