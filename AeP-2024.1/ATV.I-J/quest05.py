'''
5. Leia dois números X e N. A seguir, escreva o resultado das divisões de X por N onde, após cada
divisão, X passa a ter como conteúdo o resultado da divisão anterior e N é decrementado de 1 em 1, até
chegar a 2.
'''

def divisoes_sucessivas(x, n):
    while n >= 2:
        resultado = x / n
        print("Resultado da divisão:", resultado)
        x = resultado
        n -= 1

def main():
    x = float(input("Digite o valor de X: "))
    n = int(input("Digite o valor de N: "))
    
    divisoes_sucessivas(x, n)


main()

    