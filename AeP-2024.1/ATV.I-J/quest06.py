'''
6. Escreva um algoritmo para determinar o número de dígitos de um número informado.
'''

def contar_digitos(numero):
    contador = 0
    while numero > 0:
        numero = numero // 10 
        contador += 1
    return contador

def main():
    numero = int(input("Digite um número: "))
    quantidade_digitos = contar_digitos(numero)
    print("O número", numero, "tem", quantidade_digitos, "dígito(s).")


main()
