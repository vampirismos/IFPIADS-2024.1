'''
3. Leia 2 (dois) números, calcule e escreva o mdc (máximo divisor comum) entre os números lidos.
'''

def main():
    print("Bem-vindo a calculadora de MDC!")
    print("--------------------------------")

    numero1 = int(input("Informe o primeiro número: "))
    numero2 = int(input("Informe o segundo número: "))

    mdc = calculo_mdc(numero1,numero2)
    print(f"O MDC de {numero1} e {numero2} é igual a: {mdc}.")
    
def calculo_mdc(numero1,numero2):
    while numero2 != 0:
        temp = numero2
        numero2 = numero1 % numero2
        numero1 = temp
    return numero1


main()