# 8. Leia 2 números, calcule e escreva a divisão da soma pela subtração dos números lidos.

#Entrada
print('............................................')
nume1 = float(input("Digite o primeiro número: "))
nume2 = float(input("Digite o segundo número: "))

#Processamento
soma = nume1 + nume2
subtracao = nume2 - nume1
divisao = soma / subtracao

#Saída
print(".................................................................................")
print(f"O resultado da soma desses dois números é: {soma}")
print(f'O resultado da subtração desses dois números é: {subtracao}')
print(f'E por último, o resultado da divisão da soma pela subtração dos dois números inseridos é igual a: {divisao}.')