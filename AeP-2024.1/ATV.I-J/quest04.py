'''
4. Leia um número e divida-o por dois (sucessivamente) até que o resultado seja menor que 1. Escreva o
resultado da última divisão efetuada.
'''


def ultima_divisao(numero):
    while numero >= 1:
        numero /= 2
    return numero * 2

def main():
    numero = float(input("Digite um número: "))
    resultado = ultima_divisao(numero)
    print("Resultado da última divisão:", resultado)


main()
