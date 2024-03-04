'''
3. Leia uma letra e verifique se a letra digitada é vogal ou consoante.
'''


def main():
    letra = input("Digite uma letra: ")
    verificacao(letra.upper())


def verificacao(letra):
    if letra.upper() == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
        print ("Esta letra é uma vogal.")
    else:
        print ("Esta letra é uma consoante.")




main()