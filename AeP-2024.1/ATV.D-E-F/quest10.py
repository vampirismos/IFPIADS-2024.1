#10. Leia uma data (dia, mês e ano), verifique e escreva se a data é ou não válida.


def verificacao_data(dia, mes, ano):
    if 1 <= mes <= 12:
        if mes in [1,3,5,7,8,10,12]:
            dias_no_mes = 31
        elif mes == 2:
            dias_no_mes = 28
        else:
            dias_no_mes = 30

        if 1 <= dia <= dias_no_mes:
            return f"A data {dia}/{mes}/{ano} é válida."
        else:
            return f'A data {dia}/{mes}/{ano} não é válida. O dia está fora do intervalo para o mês.'
    else:
        return f'A data {dia}/{mes}/{ano} não é válida. O mês está fora do intervalo permitido (1-12).'
    

def main():
    dia = int(input("Informe o dia: "))
    mes = int(input("Informe o mês: "))
    ano = int(input("Informe o ano: "))
    
    resultado = verificacao_data(dia,mes,ano)
    print(resultado)


main()