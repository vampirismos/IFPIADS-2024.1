'''
14. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
1. Álcool:
· até 20 litros, desconto de 3% por litro
· acima de 20 litros, desconto de 5% por litro
2. Gasolina:
· até 20 litros, desconto de 4% por litro
· acima de 20 litros, desconto de 6% por litro.
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da
seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que
o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''

def main():
    tipo = str(input("Que cosbustivel você comprou? [A-álcool ou G-gasolina] ")).upper()
    litros = int(input("Quantos litros você comprou? "))

    if(tipo=="G"):
        if(20>=litros):
            preco = (2.5*litros) *0.97
            print(f"O valor pago pelo cliente foi de {preco}")
        else:
            preco = (2.5*litros) *0.95
            print(f"O valor pago pelo cliente foi de {preco}")

    elif(tipo=="A"):
        if(20>=litros):
            preco = (1.9*litros) *0.96
            print(f"O valor pago pelo cliente foi de {preco}")
        else:
            preco = (1.9*litros) *0.94
            print(f"O valor pago pelo cliente foi de {preco}")
    else:
        print("Digite um valor válido")
        


main()