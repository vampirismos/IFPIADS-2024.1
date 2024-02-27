'''
44. Sabendo que latão é constituído de 70% de cobre e 30% de zinco, escreva um algoritmo que calcule a
quantidade de cada um desses componentes para se obter certa quantidade de latão (em kg), informada
pelo usuário.
'''

#Entrada
quant_latao_kg = float(input("Digite a quantidade de latão desejada em kg: "))

#Processamento
quant_cobre_kg = 0.7 * quant_latao_kg
quant_zinco_kg = 0.3 * quant_latao_kg

#Saída
print(f"Para obter {quant_latao_kg}kg de latão, serão necessários:")
print(f"{quant_cobre_kg:.2f}kg de cobre e {quant_zinco_kg:.2f}kg de zinco.")
