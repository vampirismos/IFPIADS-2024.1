#18. Leia o valor do raio de uma circunferência, calcule e escreva seu comprimento.(c = 2 * p * r)

#Bibliotecas
import math

#Entrada
print("Bem-vindo a calculadora da área de uma circunferência!")
print(".....................................................")
raio = float(input("Por favor, informe o raio dessa circunferência: "))

#Processamento
area = 2 * math.pi * raio

#Saída
print("...............................................")
print(f"A área dessa circunferência é igual a: {area: .2f}.")