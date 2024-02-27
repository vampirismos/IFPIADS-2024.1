#3. Leia um valor em minutos, calcule e escreva o equivalente em horas e minutos.

#Entrada
print("Olá! Seja bem-vindo ao conversor de minutos para horas!")
print('.......................................................')
val_min = int(input("Insira o valor em minutos a ser convertido para horas e minutos, por favor: "))

#Processamento
val_hrs = val_min // 60
min_rest = val_min % 60

#Saída
print('Seu resultado foi calculado!')
print('.............................')
print(f"O valor de {val_min} após a conversão é igual a: {val_hrs} horas e {min_rest} minutos.")