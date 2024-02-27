#32. Leia um número inteiro (3 dígitos), calcule e escreva a diferença entre o número e seu inverso.

#Entrada
number = int(input("> Digite um número inteiro de 3 dígitos: "))

#Processamento
inverso = int(str(number)[::-1])
diferenca = number - inverso

#Saída
print(f"> A diferença entre o {number} e seu inverso ({inverso}) é igual a: {diferenca}.")