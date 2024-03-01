'''
29. Um número é um quadrado perfeito quando a raiz quadrada do número é igual à soma das dezenas
formadas pelos seus dois primeiros e dois últimos dígitos.
Exemplo: √9801 = 99 = 98 + 01. O número 9801 é um quadrado perfeito.
Escreva um algoritmo que leia um número de 4 dígitos e verifique se ele é um quadrado perfeito.
'''


def verificar_quadrado_perfeito(numero):
    if 1000 <= numero <= 9999:
        raiz_quadrada = int(numero ** 0.5)
        dezenas = (numero // 100) + (numero % 100)

        return raiz_quadrada == dezenas
    else:
        return False

def main():
    numero = int(input("Informe um número de 4 dígitos: "))

    resultado = verificar_quadrado_perfeito(numero)

    if resultado:
        print(f"{numero} é um quadrado perfeito.")
    else:
        print(f"{numero} não é um quadrado perfeito.")


main()
