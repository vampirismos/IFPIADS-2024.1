'''
30. Existem números de 4 dígitos (entre 1000 e 9999) que obedecem à seguinte característica: se dividirmos
o número em dois números de dois dígitos, um composto pela dezena e pela unidade, e outro pelo
milhar e pela centena, se somarmos estes dois novos números gerando um terceiro, o quadrado deste
terceiro número é exatamente o número original de quatro dígitos. Por exemplo:
2025 -> dividindo: 20 e 25 -> somando temos 45 -> 452 = 2025.
'''


def encontrar_numeros_especiais():
    numeros_especiais = []

    for numero in range(1000, 10000):
        dezena_unidade = numero % 100
        milhar_centena = numero // 100
        terceiro_numero = dezena_unidade + milhar_centena

        if terceiro_numero**2 == numero:
            numeros_especiais.append(numero)

    return numeros_especiais

def main():
    numeros_encontrados = encontrar_numeros_especiais()


    if numeros_encontrados:
        print("Números de 4 dígitos que atendem à característica:")
        for numero in numeros_encontrados: #uso de loop para evitar a fadiga
            print(numero)
    else:
        print("Não foram encontrados números que atendam à característica.")


main()
