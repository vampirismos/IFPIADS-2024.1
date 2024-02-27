#11. Leia um número inteiro (3 dígitos) e escreva o inverso do número. (Ex.: número = 532 ; inverso = 235)

#Entrada
print("..............................................................")
number = int(input("Por favor, digite um número inteiro de 3 dígitos: "))

# Processamento
invert = int(str(number)[::-1])

# Saída
print(f" O inverso do número informado é igual a: {invert}")