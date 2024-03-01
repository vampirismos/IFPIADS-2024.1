'''
18. Leia dois valores e uma das seguintes operações a serem executadas (codificadas da seguinte forma: 1 –
Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão). Calcule e escreva o resultado dessa operação
sobre os dois valores lidos. (Basicamente uma calculadora com menu de seleção :3)
'''

def realizar_operacao(valor1, valor2, operacao):
    if operacao == 1:
        resultado = valor1 + valor2
        print(f"Resultado da adição: {resultado}")
    elif operacao == 2:
        resultado = valor1 - valor2
        print(f"Resultado da subtração: {resultado}")
    elif operacao == 3:
        resultado = valor1 * valor2
        print(f"Resultado da multiplicação: {resultado}")
    elif operacao == 4:
        if valor2 != 0:
            resultado = valor1 / valor2
            print(f"Resultado da divisão: {resultado}")
        else:
            print("Não é possível dividir por zero.")
    else:
        print("Operação inválida. Por favor, escolha uma operação de 1 a 4.")

def main():
    valor1 = float(input("Informe o primeiro valor: "))
    valor2 = float(input("Informe o segundo valor: "))
    operacao = int(input("Escolha a operação (1 - Adição, 2 - Subtração, 3 - Multiplicação, 4 - Divisão): "))

    realizar_operacao(valor1, valor2, operacao)

main()
