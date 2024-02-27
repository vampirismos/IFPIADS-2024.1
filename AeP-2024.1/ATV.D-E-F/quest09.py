'''
9. Leia 1 numero entre 0 e 100 e verifique se é primo ou não.
'''

def verificacao_se_numero_primo(numero):
 if 0 <= numero <= 100:
    if numero < 2:
        print(f"{numero} não é primo.")
    elif numero == 2 or numero == 3:
        print(f"{numero} é um número primo.")
    elif numero % 2 == 0 or numero % 3 == 0:
        print(f"{numero} não é primo.")
    else:
        print(f"{numero} é primo.")
 else:
   print("O número inserido está fora do intervalo estabelecido.")

def main():
    
    numero = int(input("Informe um número dentro do intervalo entre 0-100, para verificar se ele é primo ou não: "))
    resultado = verificacao_se_numero_primo(numero)
    


main()
