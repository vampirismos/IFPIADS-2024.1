'''
5. Leia 3 (três) números e escreva-os em ordem crescente.
'''

def entrada_de_numeros():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    numero3 = float(input("Digite o terceiro número: "))
    return numero1, numero2, numero3

def organizando_numeros(numero1, numero2, numero3):
    if numero1 <= numero2 <= numero3:
        return numero1, numero2, numero3
    elif numero1 <= numero3 <= numero2:
        return numero1, numero3, numero2
    elif numero2 <= numero1 <= numero3:
        return numero2, numero1, numero3
    elif numero2 <= numero3 <= numero1:
        return numero2, numero3, numero1
    elif numero3 <= numero1 <= numero2:
        return numero3, numero1, numero2
    else:
        return numero3, numero2, numero1
    
def main():
    numero1, numero2, numero3 = entrada_de_numeros()
    numeros_organizados = organizando_numeros(numero1,numero2, numero3)

    print("Os números informados ficariam organizados da seguinte maneira em ordem decrescente: ", numeros_organizados)


main()