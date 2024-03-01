'''
28. Leia as coordenadas cartesianas (x e y) de 2 (dois) pontos no plano, que corresponderão a dois cantos de
um retângulo. Baseado nisto, calcule e escreva a área deste retângulo. Lembre-se de que o valor da área
não pode ser negativo.
'''


def calcular_area_retangulo(x1, y1, x2, y2):
    base = abs(x2 - x1)
    altura = abs(y2 - y1)

    area = base * altura

    return area

def main():
    x1 = float(input("Informe a coordenada x do primeiro ponto: "))
    y1 = float(input("Informe a coordenada y do primeiro ponto: "))
    x2 = float(input("Informe a coordenada x do segundo ponto: "))
    y2 = float(input("Informe a coordenada y do segundo ponto: "))

    area = calcular_area_retangulo(x1, y1, x2, y2)

    print(f"A área do retângulo é: {area} unidades quadradas.")



main()
