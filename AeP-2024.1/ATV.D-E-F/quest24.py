'''
24. Leia os coeficientes (A, B e C) de uma equações de 2° grau e escreva suas raízes. Vale lembrar que o
coeficiente A deve ser diferente de 0 (zero).
'''

#Bibliotecas
import math


def calcular_raizes(a, b, c):
    delta = b**2 - 4*a*c

    if delta < 0:
        return None  # Não há raízes reais
    elif delta == 0:
        raiz = -b / (2*a)
        return raiz, None  # Uma raiz real
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        return raiz1, raiz2  # Duas raízes reais

def main():
    a = float(input("Informe o coeficiente A (deve ser diferente de zero): "))
    

    if a == 0:
        print("O coeficiente A deve ser diferente de zero.")
        return

    b = float(input("Informe o coeficiente B: "))
    c = float(input("Informe o coeficiente C: "))


    raizes = calcular_raizes(a, b, c)


    if raizes is None:
        print("A equação não possui raízes reais.")
    else:
        raiz1, raiz2 = raizes
        print(f"As raízes da equação são: {raiz1} e {raiz2}")


main()
