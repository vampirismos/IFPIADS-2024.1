#37. Leia a idade de uma pessoa expressa em dias e escreva-a expressa em anos, meses e dias.

#Entrada
age_dias = int(input("Digite a idade em dias: "))

#Processamento
anos = age_dias // 365
meses = (age_dias % 365) // 30
dias = (age_dias % 365) % 30

#Saída
print(f"A idade expressa em anos, meses e dias é: {anos} anos, {meses} meses e {dias} dias.")

