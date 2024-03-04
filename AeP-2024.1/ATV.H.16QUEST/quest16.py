'''
16. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
Até 5 Kg Acima de 5 Kg
File R$ 4,90 por Kg R$ 5,80 por Kg
Alcatra R$ 5,90 por Kg R$ 6,80 por Kg
Picanha R$ 6,90 por Kg R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o
cliente receberá ainda um desconto de 5% sobre o total a compra. Escreva um programa que peça o tipo
e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da
compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
'''



def main():
    print("Você só pode levar dois tipos de carne, coloque 0 na opção que você não levará")
    file = float(input("Quantos kg de filé você comprou? "))
    alcatra = float(input("Quantos kg de alcatra você comprou? "))
    picanha = float(input("Quantos kg de picanha você comprou? "))
    cartao = str(input("Você tem o cartão da loja? (sim/não): ")).lower()
    tot = file+alcatra+picanha

    if(file<=5):
        preco_file = (4.9*file)
    else:
        preco_file = (5.8*file)
    
    if(alcatra<=5):
        preco_alcatra = (5.9*alcatra)
    else:
        preco_alcatra = (6.8*alcatra)

    if(picanha<=5):
        preco_picanha = (6.9*picanha)
    else:
        preco_picanha = (7.8*picanha)
    
    preco_tot = preco_file+preco_alcatra+preco_picanha

    if(cartao == "sim"):
        preco_desconto = preco_tot*0.9
        tipo_pagamento = "foi no Cartão Tabajara"
    else:
        tipo_pagamento = "não foi Cartão Tabajara"
        preco_desconto = preco_tot


    print(f"Foi comprado {file}kg de filé, {alcatra}kg de alcatra e {picanha}kg de picanha ")
    print(f"O preço total foi de {preco_tot}, o pagamento {tipo_pagamento}")
    print(f"O desconto foi de {(preco_tot-preco_desconto):.2f} o preço final foi de {preco_desconto}")


    

"""tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar."""
main()