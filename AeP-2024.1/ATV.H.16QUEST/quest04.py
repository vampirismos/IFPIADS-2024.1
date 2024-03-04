'''
4. Leia 2 (duas) notas parciais de um aluno, calcule a média e escreva a mensagem:
- "Aprovado", se a média alcançada for maior ou igual a sete;
- "Reprovado", se a média for menor do que sete;
- "Aprovado com Distinção", se a média for igual a dez.
'''


def calculo_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

def classificacao(media):
    if media == 10:
        print ("Aprovado com distinção.")
    elif media >= 7:
        print("Aprovado.")
    else:
        print ('Reprovado.')


def main():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = calculo_media(nota1,nota2)
    resultado = classificacao(media)
    print(resultado)


main()