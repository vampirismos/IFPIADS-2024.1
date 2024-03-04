'''
15. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
Até 5 Kg Acima de 5 Kg
Morango R$ 2,50 por Kg R$ 2,20 por Kg
Maçã R$ 1,80 por Kg R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá
ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de
morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
'''

def main():
    morango = int(input("Quantos kg de morango você comprou? "))
    maca = int(input("Quantos kg de maçã você comprou? "))
    tot = morango+maca

    if(morango<=5):
        preco_morango = (2.5*morango)
    else:
        preco_morango = (2.2*morango)
    
    if(maca<=5):
        preco_maca = (1.8*maca)
    else:
        preco_maca = (1.5*maca)
    
    preco_tot = preco_maca+preco_morango
    if(tot>8 or preco_tot>25):
        preco_tot = preco_tot*0.9

    print(f"O preço total gasto foi de {preco_tot}")
    
        


main()