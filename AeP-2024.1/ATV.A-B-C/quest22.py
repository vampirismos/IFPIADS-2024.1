#22. Leia um valor em km, calcule e escreva o equivalente em m.

#Entrada
print("Bem-vindo ao conversor de Km para M!")
print(".....................................")
val_km = float(input("Informe o valor em Km que deseja converter: "))

#Processamento
val_m = val_km * 1000

#Saída
print("....................................")
print(f"O valor {val_km} equivalente em metros é igual a: {val_m: .2f}m.")