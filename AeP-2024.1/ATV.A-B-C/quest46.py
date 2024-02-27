'''
46. Uma loja vende seus produtos no sistema entrada mais duas prestações, sendo a entrada maior ou igual a
cada uma das duas prestações; estas devem ser iguais, inteiras e as maiores possíveis. Por exemplo, se o
valor da mercadoria for R$ 270,00, a entrada e as duas prestações são iguais a R$ 90,00; se o valor da
mercadoria for R$ 302,00, a entrada é de R$ 102,00 e as duas prestações são iguais a R$ 100,00.
Escreva um algoritmo que receba o valor da mercadoria e forneça o valor da entrada e das duas
prestações, de acordo com as regras acima.
'''

#Entrada
val_mercadoria = float(input("Digite o valor da mercadoria: R$ "))

#Processamento
entrada = int(val_mercadoria / 3) + (val_mercadoria % 3)
prestacoes = int(val_mercadoria / 3)

#Saída
print(f"Para uma mercadoria de R$ {val_mercadoria:.2f}:")
print(f"Entrada: R$ {entrada:.2f}")
print(f"Prestações (2x): R$ {prestacoes:.2f}")
