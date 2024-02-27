"""
40. Calcule a quantidade de dinheiro gasta por um fumante. 
Dados de entrada: o número de anos que ele fuma, o no de cigarros
fumados por dia e o preço de uma carteira (1 carteira tem 20 cigarros).
"""

#Entrada
anos = float(input("Informe a quantidade de anos que ele fuma: "))
cig_dias = float(input("Informe a quantidade de cigarros fumados por dia: "))
cart_price = float(input("Informe o preço de uma carteira de cigarro: "))

#Processamento
cig_total = anos * 365 * cig_dias
cart_total = cig_total / 20
din_gasto = cart_total * cart_price

#Saída
print(f"O fumante gastou aproximadamente R${din_gasto:.2f} em cigarros.")