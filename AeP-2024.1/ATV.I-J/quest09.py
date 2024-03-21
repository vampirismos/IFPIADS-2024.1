'''
9. Confira o resultado de uma competição de natação entre dois clubes. O programa deve ler o número da
prova e a quantidade de nadadores. O fim dos dados é indicado pelo número da prova igual a 0 e
quantidade de nadadores igual a 0. A seguir, para cada nadador deverá ler nome, classificação, tempo,
clube (“a” ou “b”) e determinar os pontos obtidos por cada clube, de acordo com o seguinte critério:

Lugar 
1
2
3
4
Pontos
9
6
4
3

Ao final, o algoritmo deve escrever os totais de pontos de cada clube, indicando o clube vencedor.
'''



def calcular_pontuacao(classificacao):
    pontuacao = {"1": 9, "2": 6, "3": 4, "4": 3}
    return pontuacao.get(classificacao, 0)

def registrar_resultados():
    pontos_clube_a = 0
    pontos_clube_b = 0

    while True:
        num_prova = int(input("Digite o número da prova (0 para sair): "))
        if num_prova == 0:
            break
        
        quantidade_nadadores = int(input("Digite a quantidade de nadadores: "))
        
        contador = 0
        while contador < quantidade_nadadores:
            nome = input("Digite o nome do nadador: ")
            classificacao = input("Digite a classificação do nadador: ")
            tempo = float(input("Digite o tempo do nadador: "))
            clube = input("Digite o clube do nadador (a ou b): ")

            if clube == "a":
                pontos_clube_a += calcular_pontuacao(classificacao)
            elif clube == "b":
                pontos_clube_b += calcular_pontuacao(classificacao)

            contador += 1

    return pontos_clube_a, pontos_clube_b

def main():
    pontos_clube_a, pontos_clube_b = registrar_resultados()

    print("Total de pontos do Clube A:", pontos_clube_a)
    print("Total de pontos do Clube B:", pontos_clube_b)

    if pontos_clube_a > pontos_clube_b:
        print("O Clube A é o vencedor!")
    elif pontos_clube_b > pontos_clube_a:
        print("O Clube B é o vencedor!")
    else:
        print("Empate!")


main()
