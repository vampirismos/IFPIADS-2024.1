'''
11. Leia quatro números (opção, num 1, num2, num3) e que escreva o valor de num1 se opção igual a 1; o
valor de num2 se opção for igual a 2; e o valor de num3 se opção for igual a 3. Os únicos valores
possíveis para a variável opção são 1, 2 e 3.
'''

def escolher_numero(opcao, num1, num2, num3):
    if opcao == 1:
        return f'O valor escolhido é: {num1}'
    elif opcao == 2:
        return f'O valor escolhido é: {num2}'
    elif opcao == 3:
        return f'O valor escolhido é: {num3}'
    else:
        return 'Opção inválida. Escolha 1, 2 ou 3.'

def main():
    opcao = int(input("Informe a opção (1, 2 ou 3): "))
    num1 = float(input("Informe o primeiro número: "))
    num2 = float(input("Informe o segundo número: "))
    num3 = float(input("Informe o terceiro número: "))

    resultado = escolher_numero(opcao, num1, num2, num3)
    print(resultado)


main()
