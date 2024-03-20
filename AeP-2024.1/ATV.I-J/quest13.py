'''
13. Leia o salário de funcionários de uma empresa, calcule e escreva o novo salário (segundo os critérios
descritos abaixo), a soma dos salários atuais, a soma dos salários reajustados e a diferença entre as 2
somas. (Flag: salário=0)

De                     /Até          /Acréscimo
R$ 0,00                /R$ 2.999,99  /25 %
R$ 3.000,00            /R$ 5.999,99  /20 %
R$ 6.000,00            /R$ 9.999,99  /15 %
Acima de R$ 10.000,00               /10 %
'''

def calcular_reajuste(salario):
    if salario <= 2999.99:
        return salario * 1.25
    elif salario <= 5999.99:
        return salario * 1.20
    elif salario <= 9999.99:
        return salario * 1.15
    else:
        return salario * 1.10

def main():
    soma_salarios_atuais = 0
    soma_salarios_reajustados = 0
    
    while True:
        salario = float(input("Informe o salário do funcionário (ou digite 0 para encerrar): "))
        if salario == 0:
            break
        
        soma_salarios_atuais += salario
        novo_salario = calcular_reajuste(salario)
        soma_salarios_reajustados += novo_salario
        
        print(f"Novo salário: R${novo_salario:.2f}")
    
    diferenca = soma_salarios_reajustados - soma_salarios_atuais
    print("\nResumo:")
    print(f"Soma dos salários atuais: R${soma_salarios_atuais:.2f}")
    print(f"Soma dos salários reajustados: R${soma_salarios_reajustados:.2f}")
    print(f"Diferença entre as somas: R${diferenca:.2f}")



main()
