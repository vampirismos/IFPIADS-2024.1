'''
1. Leia um número e mostre na tela se o número é positivo ou negativo.
'''

#Entrada de dados
numero = int(input("Informe um número: "))


#Processamento
if numero < 0:
   print("Este número é negativo.")
elif numero == 0:
    print("Este número é o zero.")
else:
   print ("Este número é positivo.")