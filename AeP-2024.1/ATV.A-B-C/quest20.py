#20. Leia uma temperatura em °C, calcule e escreva a equivalente em °F. (t°F = (9 * t°C + 160) / 5)

#Entrada
print("Bem-vindo ao seu conversor de temperaturas que converte de Celsius para Fahrenheint!")
print("-----------------------------------------------------------------------------------")
temp_c = float(input("> Digite a temperatura em Celsius que deseja converter: "))

#Processamento
temp_f = (9 * temp_c + 160) / 5

#Saída
print(f"> A conversão de {temp_c} °C para Fahrenheint é igual a: {temp_f} °F.")