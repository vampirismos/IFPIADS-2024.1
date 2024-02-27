#38. Leia 2 (duas) frações (numerador e denominador), calcule e escreva a soma destas frações, escrevendo o resultado em forma de fração.

#Bibliotecas
from fractions import Fraction

#Entrada
numerador1 = int(input("Digite o numerador da primeira fração: "))
denominador1 = int(input("Digite o denominador da primeira fração: "))

numerador2 = int(input("Digite o numerador da segunda fração: "))
denominador2 = int(input("Digite o denominador da segunda fração: "))

#Processamento
soma = Fraction(numerador1, denominador1) + Fraction(numerador2, denominador2)

#Saída
print(f"A soma das frações é: {soma.numerator}/{soma.denominator}")