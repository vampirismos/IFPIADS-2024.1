'''
2. Leia 2 (dois) números, verifique e escreva o menor e o maior entre os números lidos.
'''

def entrada_numeros():
    print("Digite dois números e veja qual deles é maior e menor entre si!")
    numero_1 = int(input("Digite o primeiro número: "))
    numero_2 = int(input("Digite o segundo número: "))
    return numero_1, numero_2

def verificacao_maior_menor(numero_1, numero_2):
    if numero_1 > numero_2:
       maior = numero_1
       menor = numero_2
    else:
        menor = numero_1
        maior = numero_2
    return menor, maior       

def main():
    numero_1, numero_2 = entrada_numeros()
    menor, maior = verificacao_maior_menor(numero_1, numero_2)

    print(f"Este é o menor número: {menor} ")
    print (f"Este é o maior número: {maior}")


main()

