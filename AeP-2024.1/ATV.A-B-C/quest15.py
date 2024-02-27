#15. Leia o valor da base e altura de um triângulo, calcule e escreva sua área. (área=(base * altura)/2)

#Entrada
print("Vamos calcular a área de um triângulo!")
print("......................................")
base = float(input("> Por favor, digite o valor da base do triângulo: "))
altura = float(input("> Por último, informe a altura do triângulo: "))

#Processamento
area = (base * altura) / 2

#Saída
print(f"> A área do triângulo informado é igual a: {area}.")