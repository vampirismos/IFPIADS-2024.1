'''
13. Leia 5 (cinco) números inteiros e escreva o maior e o menor deles. 
Considere que todos os valores são diferentes.
'''

def obter_numero():
    return int(input("Informe um número inteiro: "))

def encontrar_maior_menor(numero, maior, menor):
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    return maior, menor

def main():
    maior = menor = obter_numero()

    for _ in range(4):             #Uso de loop para evitar a fadiga
        numero = obter_numero()
        maior, menor = encontrar_maior_menor(numero, maior, menor)

    
    print(f'O maior número é: {maior}')
    print(f'O menor número é: {menor}')


main()
