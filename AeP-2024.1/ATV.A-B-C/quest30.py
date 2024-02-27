#30. Leia um número inteiro de minutos, calcule e escreva quantos dias, quantas horas e quantos minutos ele corresponde.

#Entrada
min = int(input("> Digite um número inteiro de minutos: "))

#Processamento
dias = min // 1440
horas = (min % 1440) // 60
minutos_resto = min % 60

#Saída
print(f"> {min} minutos corresponde a: {dias} dias, {horas} horas e {minutos_resto} minutos.")
