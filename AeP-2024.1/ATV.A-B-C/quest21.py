#21. Leia uma temperatura em °F, calcule e escreva a equivalente em °C. (t°C = (5 * t°F - 160) / 9).

#Entrada
print("Bem-vindo ao seu conversor de °F para °C!")
print("-----------------------------------------")
temp_f = float(input("Por favor, informe a temperatura em °F que deseja converter: "))

#Processamento
temp_c = (5 * temp_f - 160) / 9

#Saída
print(f"{temp_f} °F é equivalente a {temp_c: .2f} °C.")