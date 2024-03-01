#12. Leia 1 (um) número inteiro e escreva se este número é par ou impar.

def verificar_paridade(numero):
    if numero % 2 == 0:
        return f'O número {numero} é par.'
    else:
        return f'O número {numero} é ímpar.'

def main():
    numero = int(input("Informe um número inteiro: "))
    resultado = verificar_paridade(numero)
    print(resultado)


main()
