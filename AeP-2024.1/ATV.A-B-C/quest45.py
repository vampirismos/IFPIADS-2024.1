'''
45. Um algoritmo para gerenciar os saques de um caixa eletrônico deve 
possuir algum mecanismo para decidir o numero de notas de cada valor que 
deve ser disponibilizado para o cliente que realizou o saque. Um possível 
critério seria o da "distribuição ótima" no sentido de que as notas de menor
valor disponíveis fossem distribuídas em número mínimo possível. Por exemplo,
se a maquina só dispõe de notas de R$ 50, de R$ 10, de R$ 5 e de R$ 1, para uma
quantia solicitada de R$ 87, o algoritmo deveria indicar uma nota de R$ 50, 
três notas de R$ 10, uma nota de R$ 5 e duas notas de R$ 1. 
Escreva um algoritmo que receba o valor da quantia solicitada e retorne a 
distribuição das notas de acordo com o critério da distribuição ótima.
'''

#Entrada
quantia_solicitada = int(input("> Digite o valor da quantia solicitada: "))

#Processamento
notas_dispon = [50, 10, 5, 1]
ctg_notas = {}

for nota in notas_dispon:
    quantidade_notas = quantia_solicitada // nota
    if quantidade_notas > 0:
        ctg_notas[nota] = quantidade_notas
        quantia_solicitada %= nota

#Saída
print(" >Distribuição ótima das notas:")
for nota, quantidade in ctg_notas.items():
    print(f"> {quantidade} nota(s) de R$ {nota}")
