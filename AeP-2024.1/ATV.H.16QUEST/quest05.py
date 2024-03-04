'''
5. Leia o preço de três produtos e informe qual produto deve ser comprado, sabendo que a decisão é
sempre pelo mais barato.
'''

def main():
    produto1 = float(input("Informe o preço do primeiro produto: "))
    produto2 = float(input("Informe o preço do segundo produto: "))
    produto3 = float(input("Informe o preço do terceiro produto: "))
    
    resultado = verificicao_preço(produto1,produto2, produto3)
    print(resultado)



def verificicao_preço(produto1, produto2, produto3):
    if produto1 < produto2 and produto1 < produto3:
        return f"De acordo com a análise, o produto de R$ {produto1} é o mais indicado para a compra."
    elif produto2 < produto1 and produto2 < produto3:
        return f"De acordo com a análise, o produto de R$ {produto2} é o mais indicado para a compra."
    else:
        return f"De acordo com a análise, o produto de R$ {produto3} é o mais indicado para a compra."
    



main()