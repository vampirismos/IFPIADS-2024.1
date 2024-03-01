'''
26. Leia os 3 (três) lados de um triângulo e identifique sua hipotenusa e seus catetos.
'''


def identificar_lados_triangulo(a, b, c):
    if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:

        if a**2 == b**2 + c**2:
            hipotenusa = a
            cateto1 = b
            cateto2 = c
        elif b**2 == a**2 + c**2:
            hipotenusa = b
            cateto1 = a
            cateto2 = c
        else:
            hipotenusa = c
            cateto1 = a
            cateto2 = b

        return hipotenusa, cateto1, cateto2
    else:
        return None  # Não é triângulo retângulo

def main():
    a = float(input("Informe o comprimento do lado A: "))
    b = float(input("Informe o comprimento do lado B: "))
    c = float(input("Informe o comprimento do lado C: "))

    lados = identificar_lados_triangulo(a, b, c)

    if lados is None:
        print("Os lados fornecidos não formam um triângulo retângulo.")
    else:
        hipotenusa, cateto1, cateto2 = lados
        print(f"A hipotenusa é {hipotenusa}, e os catetos são {cateto1} e {cateto2}.")



main()
