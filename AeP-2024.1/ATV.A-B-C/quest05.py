#5. Leia um número inteiro (3 dígitos), calcule e escreva a soma de seus elementos (C + D + U).


#Essa eu fiz no JS, mas não consegui reproduzir em python . . .

#Entrada
print(">>> Bem-vindo a calculadora de C-D-U! <<<")
print('.........................................')
numero = int(input('> Por favor, digite um número de 3 algarismos: '))

#Processamento
centena = numero / 100
resto = centena % 100
dezena = resto / 10
unidade = resto % 10
somatorio = centena + dezena + unidade

#Saída
print("> O resultado do somatório entre os três algarismos de seu número é igual a:")
print(".................................................................................")
print(f"> {centena} + {dezena} + {unidade} é igual a {somatorio: .2f}.")