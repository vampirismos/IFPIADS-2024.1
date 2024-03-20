'''
15. Leia um número (entre 0 e 255) na base decimal, calcule e escreva este número na base binária
e na base hexadecimal.
'''

def decimal_para_binario(numero):
    return bin(numero)[2:]

def decimal_para_hexadecimal(numero):
    return hex(numero)[2:].upper()

def main():
    while True:
        numero_decimal = int(input("Digite um número decimal entre 0 e 255 (ou digite -1 para sair): "))
        if numero_decimal == -1:
            break
        
        if 0 <= numero_decimal <= 255:
            binario = decimal_para_binario(numero_decimal)
            hexadecimal = decimal_para_hexadecimal(numero_decimal)
            
            print(f"Em binário: {binario}")
            print(f"Em hexadecimal: {hexadecimal}")
        else:
            print("Número fora do intervalo permitido. Por favor, digite um número entre 0 e 255.")


main()
