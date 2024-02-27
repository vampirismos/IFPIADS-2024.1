'''
1. Leia 3 (três) números, verifique e escreva quantos números iguais existem entre os números.
'''

def entrada_de_dados():
    numero_1 = float(input("Digite o primeiro número: "))
    numero_2 = float(input("Digite o segundo número: "))
    numero_3 = float(input("Digite o terceiro número: "))
    return numero_1, numero_2, numero_3

def verificacao_de_iguais(numero_1, numero_2, numero_3):
    if numero_1 == numero_2 == numero_3:
        return 3
    elif numero_1 == numero_2 or numero_1 == numero_3 or numero_2 == numero_3:
        return 2
    else:
        return 0
    

def main():
    numero_1, numero_2, numero_3 = entrada_de_dados()
    quant_de_iguais = verificacao_de_iguais(numero_1, numero_2, numero_3)

    if quant_de_iguais == 3:
       print("Os três números são iguais!")
    elif quant_de_iguais == 2:
       print("Dentre os informados, dois números são iguais!")
    else:
       print("Todos os números são diferentes!")  


main()