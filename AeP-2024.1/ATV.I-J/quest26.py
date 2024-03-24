'''
26. Cada espectador de um cinema respondeu a um questionário no qual constava sua idade e a sua opinião
em relação ao filme (1=ótimo, 2=bom, 3=regular, 4=péssimo). Escreva um algoritmo que leia a idade e
a opinião das pessoas, calcule e mostre ao final: (FLAG: idade = -1).
· a média das idades das pessoas que responderam ótimo;
· a quantidade de pessoas que respondeu regular;
· o percentual de pessoas que respondeu bom entre os entrevistados.
'''

def coletar_respostas():
    total_otimo = 0
    total_regular = 0
    total_bom = 0
    total_entrevistados = 0
    soma_idades_otimo = 0
    
    idade = 0
    
    while idade != -1:
        idade = int(input("Digite a idade (ou -1 para encerrar): "))
        
        if idade != -1:
            opiniao = int(input("Digite sua opinião em relação ao filme: "))
            total_entrevistados += 1
            
            if opiniao == 1:
                total_otimo += 1
                soma_idades_otimo += idade
            elif opiniao == 2: 
                total_bom += 1
            elif opiniao == 3:  
                total_regular += 1
    
    return total_otimo, soma_idades_otimo, total_regular, total_bom, total_entrevistados

def calcular_media_idades(total_otimo, soma_idades_otimo):
    if total_otimo > 0:
        media_idades_otimo = soma_idades_otimo / total_otimo
        return media_idades_otimo
    else:
        return None

def exibir_resultados(total_otimo, total_regular, total_bom, total_entrevistados, media_idades_otimo):
    print("----------------------------------------")
    if media_idades_otimo is not None:
        print(f"Média das idades das pessoas que responderam ótimo: {media_idades_otimo:.2f} anos")
    else:
        print("Nenhuma pessoa respondeu ótimo.")
    
    print(f"Quantidade de pessoas que responderam regular: {total_regular}")
    
    if total_entrevistados > 0:
        percentual_bom = (total_bom / total_entrevistados) * 100
        print(f"Percentual de pessoas que responderam bom: {percentual_bom:.2f}%")
    else:
        print("Nenhuma pessoa foi entrevistada.")

def main():
    print("Bem-vindo ao questionário do cinema!")
    print("......................................")
    print("Opções de avaliação:")
    print("1 - Ótimo")
    print("2 - Bom")
    print("3 - Regular")
    print("4 - Péssimo")
    print("Para encerrar o questionário, digite a idade como -1")
    print("----------------------------------------")
    
    total_otimo, soma_idades_otimo, total_regular, total_bom, total_entrevistados = coletar_respostas()
    
    media_idades_otimo = calcular_media_idades(total_otimo, soma_idades_otimo)
    
    exibir_resultados(total_otimo, total_regular, total_bom, total_entrevistados, media_idades_otimo)

main()


