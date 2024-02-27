#23. Leia um valor em kg (quilograma), calcule e escreva o equivalente em g (grama).

#Entrada
print("Vamos converter kg para grama!")
print("..............................")
quilo = float(input("Por favor, digite um valor em kg que deseja converter: "))

#Processamento
grama = quilo * 1000

#Saída
print("........................................................")
print(f"O valor de {quilo}kg em gramas é igual a: {grama: .2f}g.")