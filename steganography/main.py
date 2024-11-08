
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