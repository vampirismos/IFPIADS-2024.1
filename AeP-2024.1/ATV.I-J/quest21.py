'''
21. Leia 2 números inteiros e escreva a multiplicação dos mesmos, sem que o operador de multiplicação (*)
seja utilizado.
'''

def multiplicacao_sem_operador(num1, num2):
    resultado = 0
    i = 0
    while i < abs(num2):
        resultado += num1
        i += 1
    if num1 < 0 and num2 < 0:
        return resultado
    elif num1 < 0 or num2 < 0:
        return -resultado
    return resultado

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print("O resultado da multiplicação é:", multiplicacao_sem_operador(num1, num2))
