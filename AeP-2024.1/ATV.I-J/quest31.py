'''
31. Escreva um algoritmo que leia um número decimal (até 3 dígitos) e escreva o seu equivalente em
numeração romana. Utilize funções para obter cada dígito do número decimal e para a transformação
de numeração decimal para romana (Dica: 1 = I, 5 = V, 10 = X, 50 = L, 100 = C, 500 = D, 1.000 = M).
'''

def obter_digitos(numero):
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = (numero % 100) % 10
    return centenas, dezenas, unidades

def decimal_para_romano(digito, unidade, cinco, dez):
    if digito == 9:
        return unidade + dez
    elif digito >= 5:
        return cinco + unidade * (digito - 5)
    elif digito == 4:
        return unidade + cinco
    else:
        return unidade * digito

def converter_para_romano(numero):
    if numero < 1 or numero > 999:
        return "Número fora do intervalo válido (1 a 999)"

    centenas, dezenas, unidades = obter_digitos(numero)

    romano_centenas = decimal_para_romano(centenas, 'C', 'D', 'M')
    romano_dezenas = decimal_para_romano(dezenas, 'X', 'L', 'C')
    romano_unidades = decimal_para_romano(unidades, 'I', 'V', 'X')

    return romano_centenas + romano_dezenas + romano_unidades


numero_decimal = int(input("Digite um número decimal (até 999): "))

print("Número em numeração romana:", converter_para_romano(numero_decimal))
