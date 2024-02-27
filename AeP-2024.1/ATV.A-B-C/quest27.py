#27. Leia um número inteiro de segundos, calcule e escreva quantas horas, quantos minutos e quantos segundos ele corresponde.

#Entrada
print("> Vamos converter segundos em horas, minutos e segundos!")
sgd = int(input("> Informe o valor de segundos: "))


#Processamento
hrs = sgd // 3600
min = (sgd % 3600) // 60
sgd_rest = sgd % 60

#Saída
print(f"> {sgd}s corresponde a: {hrs}h, {min}min e {sgd_rest}s.")