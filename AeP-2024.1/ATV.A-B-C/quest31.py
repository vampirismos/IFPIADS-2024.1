#31. Leia um número inteiro (4 dígitos binários), calcule e escreva o equivalente na base decimal.

#Entrada
print ("Bem-vindo ao conversor de número binário para decimal!")
num_binario = input("> Digite um número binário de 4 dígitos: ")

#Processamento
decimal = int(num_binario, 2)

#Saída
print(f"> {num_binario} é equivalente na base decimal: {decimal}")