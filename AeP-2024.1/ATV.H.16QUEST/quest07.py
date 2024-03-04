'''
7. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe
contrataram para **desenvolver o programa que calculará os reajustes**. Escreva um algoritmo que **leia o
salário de um colaborador e o reajuste segundo o seguinte critério**, baseado no salário atual:

o salários até R$ 280,00 (incluindo) : aumento de 20%
o salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
o salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
o salários de R$ 1500,00 em diante : aumento de 5% 

Após o aumento ser realizado, **informe na tela**:
· o salário antes do reajuste;
· o percentual de aumento aplicado;
· o valor do aumento;
· o novo salário, após o aumento.
'''


def verificacao_percentual_aplicado(salario_atual):
    if salario_atual <= 280:
        percentual_aplicado = 20
    elif salario_atual <= 700:
        percentual_aplicado = 15
    elif salario_atual <= 1500:
        percentual_aplicado = 10
    else:
        percentual_aplicado = 5
    
    return percentual_aplicado


def calculo_aumento(salario_atual, percentual_aplicado):
    aumento = salario_atual * (percentual_aplicado / 100)
    return aumento


def calculo_salario_final(salario_atual, aumento):
    salario_final = salario_atual + aumento
    return salario_final



def main():
    salario_atual = float(input("Por favor, informe seu salário atual: "))
    
    percentual_aplicado = verificacao_percentual_aplicado(salario_atual)
    aumento = calculo_aumento(salario_atual, percentual_aplicado)
    salario_final = calculo_salario_final(salario_atual, aumento)

    print(f"Seu salário antes do reajuste era igual a R$ {salario_atual}.")
    print (f'O percentual de aumento aplicado foi igual a {percentual_aplicado}%.')
    print (f'O valor do aumento foi totalizado em: {aumento}.')
    print (f"No total, seu salário final será igual a R$ {salario_final: .2f}.")


main()