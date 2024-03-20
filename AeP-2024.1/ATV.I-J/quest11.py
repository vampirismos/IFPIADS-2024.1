'''
11. Leia informações de alunos (matrícula, nota1, nota2, nota3) com o fim das informações indicado por
matrícula = 0. Para cada aluno deve ser calculada a média final de acordo com a seguinte fórmula:

Média Final = (2 * nota1) + (3 * nota2) + (5 * nota3)

10

Se a média final for igual ou superior a 7, o aluno está aprovado; se a média final for inferior a 7, o
aluno está reprovado. Ao final devem ser mostrados o total de aprovados, o total de reprovados e o total
de alunos da turma.
'''


def menu_sessao():
    print('> S E S S Ã O  I N I C I A D A <')
    print("Vamos conferir sua aprovação!")
    print('------------------------------')
    
    total_aprovados = 0
    total_reprovados = 0
    total_alunos = 0
    
    while True:
        matricula = input('Informe sua matrícula por favor (ou digite 0 para sair): ')
        if matricula == '0':
            break
        
        print('Por favor, informe suas notas!')
        nota1 = float(input('Nota 1: '))
        nota2 = float(input('Nota 2: '))
        nota3 = float(input('Nota 3: '))
        
        media_final = calculo_media(nota1, nota2, nota3)
        total_alunos += 1
        
        if media_final >= 7:
            print(f'Parabéns! Você está aprovado!')
            total_aprovados += 1
        else:
            print(f"Infelizmente você não atingiu a média necessária para ser aprovado. :c")
            total_reprovados += 1
    
    print('------------------------------')
    print('Total de aprovados:', total_aprovados)
    print('Total de reprovados:', total_reprovados)
    print('Total de alunos:', total_alunos)


def calculo_media(nota1, nota2, nota3):
    return (2 * nota1) + (3 * nota2) + (5 * nota3) / 10


def main():
    menu_sessao()



main()

