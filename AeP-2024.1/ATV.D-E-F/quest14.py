'''
4. Leia 5 (cinco) números inteiros, calcule a sua média e escreva os que são maiores que a média.
'''


def obter_numero(posicao):
    return int(input(f"Informe o {posicao}º número inteiro: "))

def calcular_media(num1, num2, num3, num4, num5):
    return (num1 + num2 + num3 + num4 + num5) / 5

def maiores_que_media(num1, num2, num3, num4, num5, media):
    print("Números maiores que a média:")
    if num1 > media:
        print(num1)
    if num2 > media:
        print(num2)
    if num3 > media:
        print(num3)
    if num4 > media:
        print(num4)
    if num5 > media:
        print(num5)

def main():
    num1 = obter_numero(1)
    num2 = obter_numero(2)
    num3 = obter_numero(3)
    num4 = obter_numero(4)
    num5 = obter_numero(5)

    media = calcular_media(num1, num2, num3, num4, num5)

    maiores_que_media(num1, num2, num3, num4, num5, media)


main()
