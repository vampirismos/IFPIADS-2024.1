'''
17. Leia valores inteiros em duas variáveis distintas e se o resto da divisão da primeira pela segunda for 1
escreva a soma dessas variáveis mais o resto da divisão; se for 2 escreva se o primeiro e o segundo valor
são pares ou ímpares; se for igual a 3 multiplique a soma dos valores lidos pelo primeiro; se for igual a 4
divida a soma dos números lidos pelo segundo, se este for diferente de zero. Em qualquer outra situação
escreva o quadrado dos números lidos.
'''



def realizar_operacao(valor1, valor2):
    resto_divisao = valor1 % valor2

    if resto_divisao == 1:
        resultado = valor1 + valor2
        print(f"A soma dos valores mais o resto da divisão é: {resultado}")
    elif resto_divisao == 2:
        if valor1 % 2 == 0:
            par_impar_valor1 = "par"
        else:
            par_impar_valor1 = "ímpar"

        if valor2 % 2 == 0:
            par_impar_valor2 = "par"
        else:
            par_impar_valor2 = "ímpar"

        print(f"O primeiro valor é {par_impar_valor1} e o segundo valor é {par_impar_valor2}.")
    elif resto_divisao == 3:
        resultado = (valor1 + valor2) * valor1
        print(f"A multiplicação da soma pelos valor 1 é: {resultado}")
    elif resto_divisao == 4:
        if valor2 != 0:
            resultado = (valor1 + valor2) / valor2
            print(f"A divisão da soma pelo valor 2 é: {resultado}")
        else:
            print("Não é possível dividir por zero.")
    else:
        print(f"O quadrado do primeiro valor é {valor1**2} e o quadrado do segundo valor é {valor2**2}.")

def main():
    valor1 = int(input("Informe o primeiro valor inteiro: "))
    valor2 = int(input("Informe o segundo valor inteiro (diferente de zero): "))

    realizar_operacao(valor1, valor2)


main()
