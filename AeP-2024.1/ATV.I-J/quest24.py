'''
24. Escreva um algoritmo que leia a razão de uma PA (Progressão Aritmética) e o seu primeiro termo e
escreva os N termos da PA. Ler o valor de N.
'''

def termos_pa(primeiro_termo, razao, n):
    termos = [primeiro_termo]  
    i = 1

    while i < n: 
        proximo_termo = termos[-1] + razao 
        termos.append(proximo_termo) 
        i += 1

    return termos


razao = float(input("Digite a razão da PA: "))
primeiro_termo = float(input("Digite o primeiro termo da PA: "))
n = int(input("Digite o número de termos da PA (N): "))


termos = termos_pa(primeiro_termo, razao, n)
print("Os", n, "termos da PA são:", termos)
