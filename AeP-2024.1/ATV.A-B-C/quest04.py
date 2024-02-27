#4. Leia o valor do dólar e um valor em dólar, calcule e escreva o equivalente em real (R$).


#Entrada
print('Bem-vindo ao conversor de USD para BRL!')
print('...............==//==...............')
cotacao_usd = int(input('Por favor, informe a cotação atual do dólar:'))
val_usd = int(input('Insira o valor em dólar a ser convertido:'))

#Processamento
val_brl = val_usd * cotacao_usd

#Saída
print("..............................................................")
print(f'A conversão de {val_usd} dólares para BRL é igual a:{val_brl: .2f} reais.')