'''
8.ler data atual e data de nascimento, depois calcular sua idade.
'''

def calculo_idade(dia_nasc,mes_nasc,ano_nasc, dia_atual,mes_atual,ano_atual):
    idade = ano_atual - ano_nasc

    if mes_atual < mes_nasc or (mes_atual == mes_nasc and dia_atual < dia_nasc):
        idade -= 1

    return idade    
    


def main():
    dia_nasc = int(input("Insira o dia de nascimento: "))
    mes_nasc = int(input("Insira o mês de nascimento: "))
    ano_nasc = int(input("Insira o ano de nascimento: "))

    dia_atual = int(input("Insira o dia de atual: "))
    mes_atual = int(input("Insira o mês de atual: "))
    ano_atual = int(input("Insira o ano de atual: "))
                   
                      
    idade = calculo_idade(dia_nasc,mes_nasc,ano_nasc, dia_atual,mes_atual,ano_atual)
    print(f"Sua idade é: {idade}.")


main()
