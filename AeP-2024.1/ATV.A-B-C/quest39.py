# 39. Leia três números inteiros e positivos (A, B, C) e calcule a seguinte expressão: (r + s) /2 onde r=(a+b)² e s=(b+c)²


#Entrada
num_A = int(input("Digite o valor de A: "))
num_B = int(input("Digite o valor de B: "))
num_C = int(input("Digite o valor de C: "))

#Processamento
val_r = (num_A + num_B)**2
val_s = (num_B + num_C)**2
result = (val_r + val_s) / 2

#Saída
print(f"O resultado da expressão é igual a: {result}.")
