'''
2. Leia uma letra, verifique se letra é "F" ou "M" e escreva F - Feminino, M - Masculino, Sexo Inválido.
'''


def verificacao(letra):
    if letra.upper() == 'F':
        print("Sexo feminino.")
    elif letra.upper() == 'M':
        print("Sexo masculino.")
    else:
        print("Sexo inválido.")
    

def main():
    letra = input("Informe uma das letras (F/M): ")
    verificacao(letra.upper())

main()