'''
30. Escreva um algoritmo que leia o nome de um produto, o preço e a quantidade comprada. Escreva o
nome do produto comprado e o valor total a ser pago, considerando que são oferecidos descontos pelo
número de unidades compradas, segundo a tabela abaixo: (FLAG: nome do produto = “FIM”).
a. Até 10 unidades: valor total
b. de 11 a 20 unidades: 10% de desconto
c. de 21 a 50 unidades: 20% de desconto
d. acima de 50 unidades: 25% de desconto
'''

def calcular_valor_total(nome_produto, preco_unitario, quantidade):
    valor_total = preco_unitario * quantidade
    
    if quantidade >= 11 and quantidade <= 20:
        desconto = 0.1  
    elif quantidade >= 21 and quantidade <= 50:
        desconto = 0.2  
    elif quantidade > 50:
        desconto = 0.25  
    else:
        desconto = 0  
    
    valor_com_desconto = valor_total * (1 - desconto)
    return nome_produto, valor_com_desconto


nome_produto = ""
while nome_produto != "FIM":
    nome_produto = input("Digite o nome do produto (ou 'FIM' para sair): ")
    if nome_produto != "FIM":
        preco_unitario = float(input("Digite o preço unitário do produto: R$ "))
        quantidade = int(input("Digite a quantidade comprada do produto: "))

        produto_comprado, valor_final = calcular_valor_total(nome_produto, preco_unitario, quantidade)
        print(f"Produto: {produto_comprado}")
        print(f"Valor total a ser pago: R$ {valor_final:.2f}\n")
