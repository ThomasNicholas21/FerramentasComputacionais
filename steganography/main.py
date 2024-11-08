from ferramentas import texto_embutido
from pathlib import Path

base_dir = Path("imagens")  # Diretório onde as imagens serão salvas
base_dir.mkdir(exist_ok=True)  

image_path = base_dir / "imagem_original.png"
output_path = base_dir / "imagem_codificada.png"

def menu():
    opcoes = input(
        'Selecione:\n'
        '[1] - Embutir texto em Imagem (Steganography)\n'
        '[2] - Recuperar texto em Imagem (Steganography)\n'
        '[3] - Gerar Hash da imagem alterada (Steganography)\n'
        '[4] - Encriptar o texo encriptado (Steganography)\n'
        '[5] - Descriptar o texto encriptado (Steganography)\n'
        '[s] - Sair\n'
        '--> '
).lower()
    
    match opcoes:
        case '1':
            texto = input('Digite um texto: ')
            texto_embutido(image_path, texto, output_path)
            return False
        case '2':
            return False
        case '3':
            return False
        case '4':
            return False
        case '5':
            return False
        case 's':
            print('Encerrando sistema.')
            return True

def main():
    
    while True:
        comando = menu()
        if comando:
            break

if __name__ == '__main__':
    main()