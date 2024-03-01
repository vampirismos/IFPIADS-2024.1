

def verificar_aprovacao(nota1, nota2):
    media = (nota1 + nota2) / 2

    if media >= 7.0:
        print("Aprovado")
    else:
        nota_exame = float(input("Informe a nota do exame: "))
        media_final = (media + nota_exame) / 2

        if media_final >= 5.0:
            print("Aprovado")
        else:
            print("Reprovado")

def main():
    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))

    verificar_aprovacao(nota1, nota2)


main()
