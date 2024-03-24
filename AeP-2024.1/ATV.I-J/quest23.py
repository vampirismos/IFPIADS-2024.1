'''
23. Escreva um algoritmo que leia a razão de uma PG (Progressão Geométrica) e o seu primeiro termo e
escreva os N termos da PG. Ler o valor de N.
'''

def termos_pg(primeiro_termo, razao, n):
    termos = [primeiro_termo]  
    i = 1

    while i < n:  
        proximo_termo = termos[-1] * razao 
        termos.append(proximo_termo)  
        i += 1

    return termos


razao = float(input("Digite a razão da PG: "))
primeiro_termo = float(input("Digite o primeiro termo da PG: "))
n = int(input("Digite o número de termos da PG (N): "))


termos = termos_pg(primeiro_termo, razao, n)
print("Os", n, "termos da PG são:", termos)
