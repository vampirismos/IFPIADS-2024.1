'''
8. Para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a
11% do salário bruto, mas não é descontado (é a empresa que deposita). O salário líquido corresponde
ao salário bruto menos os descontos. **O programa deverá pedir ao usuário o valor da sua hora e a
quantidade de horas trabalhadas no mês.**

Desconto do IR:
o Salário Bruto até R$ 900,00 (inclusive) - isento
o Salário Bruto até R$ 1.500,00 (inclusive) - desconto de 5%
o Salário Bruto até R$ 2.500,00 (inclusive) - desconto de 10%
o Salário Bruto acima de R$ 2.500,00 - desconto de 20%

**Escreva na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e
a quantidade de hora é 220.**

Salário Bruto: (5 * 220) : R$ 1100,00
(-) IR (5%) : R$ 55,00
(-) INSS ( 10%) : R$ 110,00
FGTS (11%) : R$ 121,00
Total de descontos : R$ 165,00
Salário Liquido : R$ 935,00
'''


def calcular_desconto_ir(salario_bruto):
    if salario_bruto <= 900:
        return 0
    elif salario_bruto <= 1500:
        return salario_bruto * 0.05
    elif salario_bruto <= 2500:
        return salario_bruto * 0.10
    else:
        return salario_bruto * 0.20

def calcular_salario_liquido(valor_hora, horas_trabalhadas):
    salario_bruto = valor_hora * horas_trabalhadas
    desconto_ir = calcular_desconto_ir(salario_bruto)
    desconto_sindicato = salario_bruto * 0.03
    fgts = salario_bruto * 0.11
    salario_liquido = salario_bruto - desconto_ir - desconto_sindicato
    return salario_bruto, desconto_ir, desconto_sindicato, fgts, salario_liquido

def main():
    valor_hora = float(input("Informe o valor da sua hora de trabalho: "))
    horas_trabalhadas = float(input("Informe a quantidade de horas trabalhadas no mês: "))

    salario_bruto, desconto_ir, desconto_sindicato, fgts, salario_liquido = calcular_salario_liquido(valor_hora, horas_trabalhadas)

    print("\nFolha de Pagamento")
    print(f"Salário Bruto: R$ {salario_bruto:.2f}")
    print(f"Desconto do Imposto de Renda: R$ {desconto_ir:.2f}")
    print(f"Desconto do Sindicato: R$ {desconto_sindicato:.2f}")
    print(f"FGTS: R$ {fgts:.2f}")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")


main()
