'''
23. Leia 2 datas (cada data é composta por 3 variáveis inteiras: dia, mês e ano) e escreva qual delas é a mais
recente.
'''


def comparar_datas(dia1, mes1, ano1, dia2, mes2, ano2):
    if ano1 > ano2:
        return 1
    elif ano1 < ano2:
        return 2
    else:
        if mes1 > mes2:
            return 1
        elif mes1 < mes2:
            return 2
        else:
            if dia1 > dia2:
                return 1
            elif dia1 < dia2:
                return 2
            else:
                return 0  # As datas são iguais

def main():
    dia1 = int(input("Informe o dia da primeira data: "))
    mes1 = int(input("Informe o mês da primeira data: "))
    ano1 = int(input("Informe o ano da primeira data: "))

    dia2 = int(input("Informe o dia da segunda data: "))
    mes2 = int(input("Informe o mês da segunda data: "))
    ano2 = int(input("Informe o ano da segunda data: "))

    resultado = comparar_datas(dia1, mes1, ano1, dia2, mes2, ano2)

    if resultado == 0:
        print("As datas são iguais.")
    elif resultado == 1:
        print("A primeira data é mais recente.")
    else:
        print("A segunda data é mais recente.")



main()
