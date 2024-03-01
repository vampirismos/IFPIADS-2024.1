'''
20. Leia a medida de um ângulo (entre 0 e 360°) e escreva o quadrante (primeiro, segundo, terceiro ou
quarto) em que o ângulo se localiza.

iNfo: 1º quadrante: 0-90° | 2º quadrante: 90-180° | 3º quadrante: 180-270° | 4º quadrante: 270-360° 
'''


def verificacao_quadrante(angulo):
    if angulo >= 0 and angulo <= 90:
        return "Este ângulo se encontra no primeiro quadrante do plano cartesiano."
    elif angulo >= 90 and angulo <= 180:
        return "Este ângulo se encontra no segundo quadrante."
    elif angulo >= 180 and angulo <= 270:
        return "Este ângulo se encontra no terceiro quadrante."
    else:
        return "Este ângulo está no quarto quadrante."
    

def main():
    angulo = float(input("Informe um ângulo válido(entre 0° e 360°): "))
    resultado = verificacao_quadrante(angulo)
    print(resultado)

    

main()