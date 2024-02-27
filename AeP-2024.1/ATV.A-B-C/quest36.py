#36. Leia a idade de uma pessoa expressa em anos, meses e dias e escreva-a expressa apenas em dias.

#Entrada
anos = int(input("Digite a idade em anos: "))
meses = int(input("Digite a idade em meses: "))
dias = int(input("Digite a idade em dias: "))

#Processamento
idade_dias = anos * 365 + meses * 30 + dias

#Saída
print(f"A idade expressa em dias é: {idade_dias} dias.")
