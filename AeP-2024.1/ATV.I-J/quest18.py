'''
18. Supondo-se que a população de uma cidade A seja de 200.000 habitantes, com uma taxa anual de
crescimento na ordem de 3.5%, e que a população de uma cidade B seja de 800.000 habitantes,
crescendo a uma taxa anual de 1.35%, Escreva um algoritmo que determine quantos anos serão
necessários, para que a população da cidade A ultrapasse a população da cidade B.
'''

def main():
    populacao_a = 200000
    populacao_b = 800000
    anos = 0

    while (populacao_a < populacao_b):
        populacao_a += populacao_a * (3.5 / 100)
        populacao_b += populacao_b * (1.35 / 100)
        anos += 1
        print(f"População A: {populacao_a: .2f} e população B: {populacao_b: .2f}. Anos passados {anos}")

    print(f"Demoraria {anos} anos para a população da cidade A ultrapassar a da cidade B.")



main()