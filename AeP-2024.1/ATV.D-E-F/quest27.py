'''
27. Determine a idade de uma pessoa, em anos, meses e dias, dadas a data (dia, mês e ano) do seu
nascimento e a data (dia, mês e ano) atual.
'''

#Bibliotecas
from datetime import datetime


def calcular_idade(dia_nasc, mes_nasc, ano_nasc, dia_atual, mes_atual, ano_atual):
    data_nascimento = datetime(ano_nasc, mes_nasc, dia_nasc)
    data_atual = datetime(ano_atual, mes_atual, dia_atual)

    diferenca = data_atual - data_nascimento

    anos = diferenca.days // 365
    meses = (diferenca.days % 365) // 30
    dias = (diferenca.days % 365) % 30

    return anos, meses, dias

def main():
    dia_nasc = int(input("Informe o dia de nascimento: "))
    mes_nasc = int(input("Informe o mês de nascimento: "))
    ano_nasc = int(input("Informe o ano de nascimento: "))

    dia_atual = int(input("Informe o dia atual: "))
    mes_atual = int(input("Informe o mês atual: "))
    ano_atual = int(input("Informe o ano atual: "))

    idade = calcular_idade(dia_nasc, mes_nasc, ano_nasc, dia_atual, mes_atual, ano_atual)

    print(f"A idade é de {idade[0]} anos, {idade[1]} meses e {idade[2]} dias.")



main()
