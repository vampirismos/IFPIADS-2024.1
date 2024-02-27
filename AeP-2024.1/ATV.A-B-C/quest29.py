#29. Leia um número inteiro de meses, calcule e escreva quantos anos e quantos meses ele corresponde.

#Entrada
meses = int(input("> Digite uma quantidade inteira de meses: "))

#Processamento
anos = meses // 12
meses_rest = meses % 12

#Saída
print(f"{meses} meses corresponde a: {anos} anos e {meses_rest} meses.")