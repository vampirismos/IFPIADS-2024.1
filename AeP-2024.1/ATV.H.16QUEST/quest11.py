'''
11. Leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do
número. Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplos:
o 326 = 3 centenas, 2 dezenas e 6 unidades
o 12 = 1 dezena e 2 unidades
'''

#Bibliotecas
import math


def main():
    numero = int(input("Digite um número entre 0 e 1000: "))
    cent = math.floor(numero/100)
    deze = (numero%100)//10
    unid = numero%10
    print(cent, deze, unid)
    a =''
    b =''
    c =''
    if numero<1000:
        if(cent == 1):
            a = " centena"
        if(deze == 1):
            b = " dezena"
        if(unid == 1):
            c = " unidade"
        if(cent > 1):
            a = " centenas"
        if(deze > 1):
            b = " dezenas"
        if(unid > 1):
            c = " unidades"

        if(cent>0 and deze>0 and unid>0):
            print(f"{numero} = {cent}{a}, {deze}{b} e {unid}{c}")

        elif(cent==0 and deze==0 and unid>1):
            print(f"{numero} = {unid}{c}")
        
        elif(cent==0 and deze>0 and unid==0):
            print(f"{numero} = {deze}{b}")

        elif(cent==0 and deze>0 and unid>0):
            print(f"{numero} = {deze}{b} e {unid}{c}")
        
        elif(cent>0 and deze==0 and unid==0):
            print(f"{numero} = {cent}{a}")

        elif(cent>0 and deze==0 and unid>0):
            print(f"{numero} = {cent}{a} e {unid}{c}")
    
    else:
        print("Escreva um numero menor que 1000")
                
main()