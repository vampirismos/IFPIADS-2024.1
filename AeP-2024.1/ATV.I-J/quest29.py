'''
29. Escreva um algoritmo que calcula o retorno de um investimento financeiro. O usuário deve informar
quanto será investido por mês e qual será a taxa de juros mensal. O algoritmo deve informar o saldo do
investimento após um ano (soma das aplicações mensais + juros compostos), e perguntar ao usuário se
deseja calcular o ano seguinte, sucessivamente. Por exemplo, caso o usuário deseje investir R$ 100,00
por mês, e tenha uma taxa de juros de 1% ao mês, o algoritmo forneceria a seguinte saída:
Saldo do investimento após 1 ano: 1268.25
Deseja processar mais um ano (S/N) ?
'''

def calcula_retorno_investimento(investimento_mensal, taxa_juros_mensal):
    saldo = 0
    meses = 0
    while meses < 12:  
        saldo += investimento_mensal  
        saldo *= (1 + taxa_juros_mensal)  
        meses += 1

    return saldo

continuar = 'S'
while continuar == 'S':
    investimento_mensal = float(input("Informe o valor a ser investido por mês: R$ "))
    taxa_juros_mensal = float(input("Informe a taxa de juros mensal (em decimal): "))
    
    saldo_final = calcula_retorno_investimento(investimento_mensal, taxa_juros_mensal)
    print(f"Saldo do investimento após 1 ano: R$ {saldo_final:.2f}")

    continuar = input("Deseja processar mais um ano (S/N) ? ").strip().upper()
