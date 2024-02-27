'''
7. verificar se escaleno, isosceles ou equilatero.
'''

def verificacao_tipo_de_triangulo(lado1, lado2, lado3):
    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
        if lado1 == lado2 == lado3:
            return "Triângulo equilátero."
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            return "Triângulo isósceles."
        else:
            return "Triângulo escaleno."
    else:
        return "Não formam um triângulo."
    
def main():
    lado1 = float(input("Informe o comprimento do primeiro lado: "))
    lado2 = float(input("Informe o comprimento do segundo lado: "))
    lado3 = float(input("Informe o comprimento do terceiro lado: "))

    resultado = verificacao_tipo_de_triangulo(lado1,lado2, lado3)
    print(resultado)
    

main()