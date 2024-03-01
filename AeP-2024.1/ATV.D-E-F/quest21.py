'''
21. Realize arredondamentos de números utilizando a regra usual da matemática: se a parte fracionaria for
maior do que ou igual a 0,5, o numero é arredondado para o inteiro imediatamente superior, caso
contrario, é arredondado para o inteiro imediatamente inferior.
'''


def calcular_parte_fracionaria(numero):
    return numero - int(numero)

def arredondar_numero(numero):
    parte_fracionaria = calcular_parte_fracionaria(numero)

    if parte_fracionaria >= 0.5:
        return int(numero) + 1
    else:
        return int(numero)

def main():
    numero = float(input("Informe um número para arredondar: "))
    resultado = arredondar_numero(numero)
    print(f"O número arredondado é: {resultado}")



main()
