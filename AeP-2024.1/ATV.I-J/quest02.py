'''
2. Leia 2 (dois) números, calcule e escreva o mmc (mínimo múltiplo comum) entre os números lidos.
'''

def main():
     numero1 = int(input("Informe o primeiro número: "))
     numero2 = int(input("Informe o segundo número: "))

     mmc = calculo_mmc(numero1,numero2)
     print(f"O MMC de {numero1} e {numero2} é igual a: {mmc}")

def calculo_mmc(numero1, numero2):
    if numero1 > numero2:
        maior = numero1
    else:
        maior = numero2
    
    while(True):
        if  maior % numero1 == 0 and maior % numero2 == 0:
            mmc = maior
            break
        maior +=1
    return mmc



main()