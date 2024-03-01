'''
15. Leia a quantidade de horas aula dadas por dois professores 
e o valor por hora recebido por cada um. Escreva na tela qual 
dos professores tem salário total maior.
'''

def calcular_salario_total(horas_aula, valor_por_hora):
    return horas_aula * valor_por_hora

def main():
    horas_aula_professor1 = float(input("Informe as horas aula do primeiro professor: "))
    valor_por_hora_professor1 = float(input("Informe o valor por hora do primeiro professor: "))

    horas_aula_professor2 = float(input("Informe as horas aula do segundo professor: "))
    valor_por_hora_professor2 = float(input("Informe o valor por hora do segundo professor: "))

    salario_total_professor1 = calcular_salario_total(horas_aula_professor1, valor_por_hora_professor1)
    salario_total_professor2 = calcular_salario_total(horas_aula_professor2, valor_por_hora_professor2)

    if salario_total_professor1 > salario_total_professor2:
        print("O primeiro professor tem um salário total maior.")
    elif salario_total_professor1 < salario_total_professor2:
        print("O segundo professor tem um salário total maior.")
    else:
        print("Ambos os professores têm salários totais iguais.")


main()
