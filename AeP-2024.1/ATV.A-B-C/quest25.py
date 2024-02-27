#25. Leia um número inteiro de metros, calcule e escreva quantos Km e quantos metros ele corresponde.

#Entrada
print('Quer saber quantos metros equivalem a km e metros? Posso ajudar!')
metros = float(input("Informe um valor em metros a ser convertido: "))

#Processamento
kilom = metros // 1000
rest_m = metros % 1000

#Saída
print(f"{metros} metros é equivalente a: {kilom: .2f}km e {rest_m: .2f}m.")
