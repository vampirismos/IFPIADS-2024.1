'''
41. O custo ao consumidor de um carro novo é a soma do custo de fábrica 
com a percentagem do distribuidor e dos impostos (aplicados ao custo de 
fábrica). Supondo que a percentagem do distribuidor seja de 28% e os 
impostos de 45%, escreva um algoritmo que leia o custo de fábrica de um carro e
escreva o custo ao consumidor.
'''

#Entrada
custo_fabrica = float(input("> Digite o custo de fábrica do carro: "))

#Processamento
porcent_distrib = 0.28
impostos = 0.45
custo_consumidor = custo_fabrica + (custo_fabrica * porcent_distrib) + (custo_fabrica * impostos)

#Saída
print(f"> O custo ao consumidor do carro é equivalente a: R${custo_consumidor:.2f}.")
