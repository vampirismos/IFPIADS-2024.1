#24. Leia um valor em m, calcule e escreva o equivalente em cm.

#Entrada
print("Precisa de ajuda para converter metros para centímetros? Posso ajudar!")
metros = float(input("> Primeiramente, informe um valor em metros a ser convertido: "))
print("...............................................................................")

#Processamento
centi = metros * 100

#Saída
print(f"> O resultado da conversão de {metros}m para centímetros é igual a: {centi: .2f}cm.")
