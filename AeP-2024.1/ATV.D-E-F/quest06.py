'''
6. Leia 3 (três) números (cada número corresponde a 
um ângulo interno do triângulo), verifique e escreva
se os 3 (três) números formam um triângulo 
(a soma dos ângulos internos é igual a 180o). 

Se formam,verifique se formam um triângulo acutângulo (3 ângulos < 90o), 
retângulo (1 ângulo = 90o) ou obtusângulo (1 ângulo > 90o). 
'''

def verificacao_se_triangulo(angulo1, angulo2, angulo3):
    soma_angulos = angulo1 + angulo2 + angulo3
    
    if soma_angulos == 180:
        if angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
            return "Triângulo acutângulo!"
        elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
            return "Triângulo retângulo!"
        else:
            return "Triângulo obtusângulo!"
    else:
        return "Não forma um triângulo."

def main():
    angulo1 = float(input("Digite o primeiro ângulo: ")) 
    angulo2 = float(input("Digite o segundo ângulo: ")) 
    angulo3 = float(input("Digite o terceiro ângulo: "))         

    resultado = verificacao_se_triangulo(angulo1,angulo2,angulo3)
    
    
    print(resultado)


main()

