'''
16. Uma companhia financeira debita um juro de 0.85% diário sobre o saldo não pago de um empréstimo.
Com um empréstimo de R$ 3.000,00, um pagamento de R$ 200,00 é feito todo dia útil. Escreva um
algoritmo que calcule quantos dias úteis são necessários para se concluir o pagamento do empréstimo.
'''


def calcular_dias_uteis(emprestimo, pagamento_diario):
    saldo = emprestimo
    dias_uteis = 0
    
    while saldo > 0:
        saldo -= pagamento_diario
        saldo *= 1 + 0.0085
        dias_uteis += 1
    
    return dias_uteis

def main():
    emprestimo = 3000.00
    pagamento_diario = 200.00
    
    dias_necessarios = calcular_dias_uteis(emprestimo, pagamento_diario)
    
    print(f"São necessários {dias_necessarios} dias úteis para concluir o pagamento do empréstimo.")



main()
