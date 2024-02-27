#33. Leia um número inteiro (3 dígitos), calcule e escreva a soma do número com seu inverso.(Ex.: número = 532 ; inverso = 235 ; soma = 532 + 235 = 767).

#Entrada
number = int(input("> Digite um número inteiro de 3 dígitos: "))

#Processamento
inverse = int(str(number)[::-1])
somatorio = number + inverse
    
#Saída
print(f"> Soma do {number} com seu inverso ({inverse}): {somatorio}.")
