#7. Leia 3 números, calcule e escreva a soma dos 2 primeiros e a diferença entre os 2 últimos.


#Entrada
print(".......................................................")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input('Digite o terceiro número: '))

#Processamento
somatorio = num1 + num2
diferenca = num2 - num3

#Saída
print(".......................................................")
print(f"O somatório dos dois primeiros números é: {somatorio}")
print(f'A diferença entre os dois últimos números é: {diferenca}')