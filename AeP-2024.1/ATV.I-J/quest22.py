'''
22. Leia 2 números inteiros e escreva o quociente e o resto da divisão dos mesmos, sem que os operadores
de divisão (/ e %) sejam utilizados.
'''


def divisao_sem_operador(dividendo, divisor):
    quociente = 0
    resto = 0
    
    if divisor == 0:
        print("Erro: Divisão por zero!")
        return None, None
    
    negativo = False
    if (dividendo < 0 and divisor > 0) or (dividendo > 0 and divisor < 0):
        negativo = True

    dividendo = abs(dividendo)
    divisor = abs(divisor)

    while dividendo >= divisor:
        dividendo -= divisor
        quociente += 1

    resto = dividendo

    if negativo:
        quociente = -quociente
        resto = -resto

    return quociente, resto

dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))

quociente, resto = divisao_sem_operador(dividendo, divisor)
if quociente is not None and resto is not None:
    print("Quociente:", quociente)
    print("Resto:", resto)
