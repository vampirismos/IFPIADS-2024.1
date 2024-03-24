'''
25. Foi feita uma pesquisa de audiência de canal de TV em várias casas em Teresina, num certo dia. Para
cada casa visitada, o entrevistado informou o número do canal (2, 4, 5, 7, 10) e o número de pessoas que
estavam assistindo TV. Escreva um algoritmo que **leia um número indeterminado de dados (terminando
quando for lido um canal igual a zero)** e **calcule o percentual de audiência para cada emissora**,
mostrando ao final, o número de cada canal e sua respectiva audiência.
'''

def main():
    print("Bem-vindo à pesquisa de audiência de canal de TV em Teresina!")
    print("................................................................")
    print("Canais disponíveis:")
    print("Para o canal 2 digite: 2")
    print("Para o canal 4 digite: 4")
    print("Para o canal 5 digite: 5")
    print("Para o canal 7 digite: 7")
    print("Para o canal 10 digite: 10")
    print("Para encerrar a pesquisa digite: 0")
    
    votos_canal2 = 0
    votos_canal4 = 0
    votos_canal5 = 0
    votos_canal7 = 0
    votos_canal10 = 0
    total_telespectadores = 0
    
    canal_votado = -1
    
    while canal_votado != 0:
        canal_votado = int(input("Digite o número do canal assistido (ou 0 para encerrar): "))
        if canal_votado != 0:
            telespectadores = int(input("Informe o número de pessoas assistindo TV: "))
            total_telespectadores += telespectadores  
            
            if canal_votado == 2:
                votos_canal2 += telespectadores
            elif canal_votado == 4:
                votos_canal4 += telespectadores
            elif canal_votado == 5:
                votos_canal5 += telespectadores
            elif canal_votado == 7:
                votos_canal7 += telespectadores
            elif canal_votado == 10:
                votos_canal10 += telespectadores
            else:
                print("Canal inválido")
    
    percent_canal2, percent_canal4, percent_canal5, percent_canal7, percent_canal10 = calculo_percentual(votos_canal2, votos_canal4, votos_canal5, votos_canal7, votos_canal10, total_telespectadores)
    
    resultado_pesquisa(votos_canal2, votos_canal4, votos_canal5, votos_canal7, votos_canal10, percent_canal2, percent_canal4, percent_canal5, percent_canal7, percent_canal10)

def calculo_percentual(votos_canal2, votos_canal4, votos_canal5, votos_canal7, votos_canal10, total_telespectadores):
    percent_canal2 = (votos_canal2 / total_telespectadores) * 100
    percent_canal4 = (votos_canal4 / total_telespectadores) * 100
    percent_canal5 = (votos_canal5 / total_telespectadores) * 100
    percent_canal7 = (votos_canal7 / total_telespectadores) * 100
    percent_canal10 = (votos_canal10 / total_telespectadores) * 100

    return percent_canal2, percent_canal4, percent_canal5, percent_canal7, percent_canal10

def resultado_pesquisa(votos_canal2, votos_canal4, votos_canal5, votos_canal7, votos_canal10, percent_canal2, percent_canal4, percent_canal5, percent_canal7, percent_canal10):
    print("R E S U L T A D O  P E S Q U I S A :")
    print(f"Canal 2: {votos_canal2} votos - {percent_canal2:.2f}% de audiência")
    print(f"Canal 4: {votos_canal4} votos - {percent_canal4:.2f}% de audiência")
    print(f"Canal 5: {votos_canal5} votos - {percent_canal5:.2f}% de audiência")
    print(f"Canal 7: {votos_canal7} votos - {percent_canal7:.2f}% de audiência")
    print(f"Canal 10: {votos_canal10} votos - {percent_canal10:.2f}% de audiência")

main()


    

