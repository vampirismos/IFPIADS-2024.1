
#Bibliotecas
import math

#Entrada
print("Vamos calcular a distãncia entre dois pontos em um plano!")
x1 = float(input("> Digite a coordenada x do ponto 1: "))
y1 = float(input("> Digite a coordenada y do ponto 1: "))
x2 = float(input("> Digite a coordenada x do ponto 2: "))
y2 = float(input("> Digite a coordenada y do ponto 2: "))

#Processamento
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Imprime o resultado
print(f"> A distância entre os pontos ({x1}, {y1}) e ({x2}, {y2}) é igual a: {distancia: .2f}.")
