'''
28. Escreva um algoritmo que gere um número aleatório inteiro (utilize a função rand(): aleatorio = rand())
e solicite um número ao usuário. O objetivo é que o usuário acerte o número gerado. Se o número
digitado for menor que o gerado, escreva “Maior”, se for maior, escreva “Menor”, e solicite novamente
um número ao usuário. Repita este processo ate que o usuário acerte o número gerado. Após isso,
escreva em quantas tentativas o usuário acertou.
'''

import random

def jogo_adivinhacao():
    numero_aleatorio = random.randint(1, 100)
    tentativas = 0

    while True:
        tentativa = int(input("Tente adivinhar o número (entre 1 e 100): "))
        tentativas += 1

        if tentativa < numero_aleatorio:
            print("Maior")
        elif tentativa > numero_aleatorio:
            print("Menor")
        else:
            print("Parabéns! Você acertou em", tentativas, "tentativas.")
            break

jogo_adivinhacao()
