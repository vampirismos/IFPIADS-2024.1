'''
4. Leia 1 (um) número de 2 (dois) dígitos, verifique e escreva se o algarismo da dezena é igual ou diferente
do algarismo da unidade.
'''

def ler_numero_dois_digitos():
    numero = int(input("Digite um número de dois dígitos: "))
    while not (10 <= numero <= 99):
        print("Por favor, digite um número de dois dígitos.")
        numero = int(input("Digite um número de dois dígitos: "))
    return numero

def verificar_algarismos(numero):
    dezena = numero // 10
    unidade = numero % 10

    if dezena == unidade:
        return "O algarismo da dezena é igual ao algarismo da unidade."
    else:
        return "O algarismo da dezena é diferente do algarismo da unidade."

def main():
    numero = ler_numero_dois_digitos()
    resultado = verificar_algarismos(numero)
    print(resultado)


main()
