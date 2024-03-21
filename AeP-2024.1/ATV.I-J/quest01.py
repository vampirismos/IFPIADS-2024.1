'''
01. Leia uma lista de números e que cada número lido escreve o próprios número e a relação de seu divisores.
'''
lista = []

numero = int(input("Informe um número: "))

contador = 1


while(True):
    if numero %  contador == 0:
        lista.append(contador)

    contador += 1

    if contador > numero:
        break


print(lista)