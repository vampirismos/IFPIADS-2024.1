'''
27. Escreva um algoritmo que leia um conjunto de dados de um grupo de 100 pessoas, sexo (1=Masculino,
2=Feminino), idade e estado civil (1=Casado, 2=Solteiro, 3=Divorciado, 4=Viúvo) e escreva:
· Média de idade das mulheres;
· Média de idade dos homens;
· O percentual de homens solteiros;
· O percentual de mulheres solteiras;
· A quantidade de mulheres divorciadas acima de 30 anos.
'''


def calcular_estatisticas_pessoas(dados_pessoas):
    total_mulheres = 0
    total_idade_mulheres = 0
    total_homens = 0
    total_idade_homens = 0
    total_homens_solteiros = 0
    total_mulheres_solteiras = 0
    total_mulheres_divorciadas_acima_30 = 0
    
    index = 0
    while index < len(dados_pessoas):
        pessoa = dados_pessoas[index]
        sexo, idade, estado_civil = pessoa

        if sexo == 1: 
            total_homens += 1
            total_idade_homens += idade
            if estado_civil == 2: 
                total_homens_solteiros += 1
        else:
            total_mulheres += 1
            total_idade_mulheres += idade
            if estado_civil == 2:  
                total_mulheres_solteiras += 1
            if estado_civil == 3 and idade > 30:
                total_mulheres_divorciadas_acima_30 += 1

        index += 1

    media_idade_mulheres = total_idade_mulheres / total_mulheres if total_mulheres > 0 else 0
    media_idade_homens = total_idade_homens / total_homens if total_homens > 0 else 0
    percentual_homens_solteiros = (total_homens_solteiros / total_homens) * 100 if total_homens > 0 else 0
    percentual_mulheres_solteiras = (total_mulheres_solteiras / total_mulheres) * 100 if total_mulheres > 0 else 0

    return (media_idade_mulheres, media_idade_homens, percentual_homens_solteiros,
            percentual_mulheres_solteiras, total_mulheres_divorciadas_acima_30)


dados_pessoas = []


index = 0
while index < 100:
    sexo = int(input(f"Digite o sexo da {index + 1}ª pessoa (1=Masculino, 2=Feminino): "))
    idade = int(input(f"Digite a idade da {index + 1}ª pessoa: "))
    estado_civil = int(input(f"Digite o estado civil da {index + 1}ª pessoa (1=Casado, 2=Solteiro, 3=Divorciado, 4=Viúvo): "))
    dados_pessoas.append((sexo, idade, estado_civil))
    index += 1


media_idade_mulheres, media_idade_homens, percentual_homens_solteiros, percentual_mulheres_solteiras, total_mulheres_divorciadas_acima_30 = calcular_estatisticas_pessoas(dados_pessoas)

print("Média de idade das mulheres:", media_idade_mulheres)
print("Média de idade dos homens:", media_idade_homens)
print("Percentual de homens solteiros:", percentual_homens_solteiros)
print("Percentual de mulheres solteiras:", percentual_mulheres_solteiras)
print("Quantidade de mulheres divorciadas acima de 30 anos:", total_mulheres_divorciadas_acima_30)
