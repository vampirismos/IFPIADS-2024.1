#34. Leia 3 números, calcule e escreva a média dos números.

#Entrada
print("Digite 3 números para calcular a média: ")
numero1 = float(input("> Digite o primeiro número: "))
numero2 = float(input("> Digite o segundo número: "))
numero3 = float(input("> Digite o terceiro número: "))

#Processamento
media = (numero1 + numero2 + numero3) / 3

#Saída
input(f"> A média desses números é igual a: {media: .2f}.")