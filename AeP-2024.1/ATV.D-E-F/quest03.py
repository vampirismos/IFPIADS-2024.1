'''
3. Leia 3 (três) números, verifique e escreva o maior entre os números lidos.
'''

def entrada_de_numeros():
    print("Digitando três números, verifique automaticamente qual deles é menor ou maior entre si!")
    numero_um = float(input("Digite o primeiro número: "))
    numero_dois = float(input("Digite o segundo número: "))
    numero_tres = float(input("Digite o terceiro número: "))
    return numero_um, numero_dois, numero_tres


def processamento_de_dados(numero_um, numero_dois, numero_tres):
    if numero_um >= numero_dois and numero_um >= numero_tres:
     return numero_um
    elif numero_dois >= numero_um and numero_dois >= numero_tres:
     return numero_dois
    else:
       return numero_tres 
    

def main():
   numero_um, numero_dois, numero_tres = entrada_de_numeros()
   maior_numero = processamento_de_dados(numero_um,numero_dois, numero_tres)

   print(f"Dentre os números informados, o maior é: {maior_numero}!")


main()
        