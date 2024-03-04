'''
6. Leia o turno em que um aluno estuda, sendo M para matutino, V para Vespertino ou N para Noturno e
escreva a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''

def main():
    turno = input("Informe seu turno ( M | V | N ): ")

    resultado = checagem_turno(turno)
    print(resultado)


def checagem_turno(turno):
    if turno.upper() == 'M':
        return 'Bom dia!'
    elif turno.upper() == 'V':
        return 'Boa tarde!'
    elif turno.upper() == 'N':
        return 'Boa noite!'
    else:
        return "Turno inválido."
    

main()