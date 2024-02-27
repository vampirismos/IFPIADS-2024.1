#35. Leia um número inteiro (4 dígitos), calcule e escreva a soma dos elementos que o compõem. Ex.:número = 9534 ; soma = 9+5+3+4 = 21.

#Entrada
numero = int(input("Digite um número inteiro de 4 dígitos: "))

#Processamento
digitos = [int(digito) for digito in str(numero)]
soma = sum(digitos)

#Saída
print(f"A soma dos elementos de {numero} resulta em: {soma}.")
