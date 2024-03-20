'''
14. Emita o resultado de uma pesquisa de opinião pública a respeito das eleições presidenciais. O
entrevistado deverá escolher entre 3 candidatos (Serra=45, Dilma=13 ou Ciro Gomes=23), ou então
responder: indeciso=99, outros=98, nulo/branco=0. O algoritmo deve ler a opinião de voto de cada
entrevistado, encerrando-se a pesquisa com a opinião sendo igual a –1. Ao final, devem ser mostrados:
· a porcentagem de cada candidato;
· a porcentagem dos outros candidatos;
· a porcentagem de eleitores indecisos;
· a porcentagem de votos nulos/brancos;
· o total de entrevistados;
· uma mensagem indicando a possibilidade ou não de haver 2o turno.
'''

def coletar_votos():
    votos_serra = 0
    votos_dilma = 0
    votos_ciro = 0
    votos_outros = 0
    votos_indecisos = 0
    votos_nulos = 0
    total_entrevistados = 0
    
    while True:
        voto = int(input("Digite o número correspondente ao candidato: "))
        
        if voto == -1:
            break
        
        total_entrevistados += 1
        
        if voto == 45:
            votos_serra += 1
        elif voto == 13:
            votos_dilma += 1
        elif voto == 23:
            votos_ciro += 1
        elif voto == 98:
            votos_outros += 1
        elif voto == 99:
            votos_indecisos += 1
        elif voto == 0:
            votos_nulos += 1
        else:
            print("Opção inválida. Por favor, escolha um número correspondente a um candidato ou opção.")
    
    return votos_serra, votos_dilma, votos_ciro, votos_outros, votos_indecisos, votos_nulos, total_entrevistados

def calcular_porcentagens(votos_serra, votos_dilma, votos_ciro, votos_outros, votos_indecisos, votos_nulos, total_entrevistados):
    porcentagem_serra = (votos_serra / total_entrevistados) * 100
    porcentagem_dilma = (votos_dilma / total_entrevistados) * 100
    porcentagem_ciro = (votos_ciro / total_entrevistados) * 100
    porcentagem_outros = (votos_outros / total_entrevistados) * 100
    porcentagem_indecisos = (votos_indecisos / total_entrevistados) * 100
    porcentagem_nulos = (votos_nulos / total_entrevistados) * 100
    
    return porcentagem_serra, porcentagem_dilma, porcentagem_ciro, porcentagem_outros, porcentagem_indecisos, porcentagem_nulos

def verificar_segundo_turno(votos_serra, votos_dilma, votos_ciro, total_entrevistados):
    votos_validos = votos_serra + votos_dilma + votos_ciro
    if votos_validos < total_entrevistados / 2:
        segundo_turno = True
    else:
        segundo_turno = False
    
    return segundo_turno

def exibir_resultados(porcentagem_serra, porcentagem_dilma, porcentagem_ciro, porcentagem_outros, porcentagem_indecisos, porcentagem_nulos, total_entrevistados, segundo_turno):
    print("\nResultados da pesquisa:")
    print(f"Porcentagem de votos para Serra: {porcentagem_serra:.2f}%")
    print(f"Porcentagem de votos para Dilma: {porcentagem_dilma:.2f}%")
    print(f"Porcentagem de votos para Ciro Gomes: {porcentagem_ciro:.2f}%")
    print(f"Porcentagem de votos para outros candidatos: {porcentagem_outros:.2f}%")
    print(f"Porcentagem de eleitores indecisos: {porcentagem_indecisos:.2f}%")
    print(f"Porcentagem de votos nulos/brancos: {porcentagem_nulos:.2f}%")
    print(f"Total de entrevistados: {total_entrevistados}")
    
    if segundo_turno:
        print("\nHá possibilidade de haver segundo turno.")
    else:
        print("\nNão há possibilidade de haver segundo turno.")

def main():
    print("Bem-vindo a pesquisa de intenção de voto para as eleições presidencias.")
    print("""Instrunções:
          Para votar basta digitar o código de cada candidato;
          Para votar SERRA digite: 45
          Para votar DILMA digite: 13
          Para votar CIRO GOMES digite: 23
          
          Existem também as opções a seguir em caso de dúvida:
          Pra votar INDECISO digite: 99
          Para votar OUTROS digite: 98
          Para votar NULO/BRANCO digite: 0
          
          Para encerrar a pesquisa digite: -1.""")
    
          
    votos_serra, votos_dilma, votos_ciro, votos_outros, votos_indecisos, votos_nulos, total_entrevistados = coletar_votos()
    
    porcentagem_serra, porcentagem_dilma, porcentagem_ciro, porcentagem_outros, porcentagem_indecisos, porcentagem_nulos = calcular_porcentagens(votos_serra, votos_dilma, votos_ciro, votos_outros, votos_indecisos, votos_nulos, total_entrevistados)
    
    segundo_turno = verificar_segundo_turno(votos_serra, votos_dilma, votos_ciro, total_entrevistados)
    
    exibir_resultados(porcentagem_serra, porcentagem_dilma, porcentagem_ciro, porcentagem_outros, porcentagem_indecisos, porcentagem_nulos, total_entrevistados, segundo_turno)


main()
