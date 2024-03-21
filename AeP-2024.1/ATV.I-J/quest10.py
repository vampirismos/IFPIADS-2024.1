'''
10. Calcule a quantidade de combustível que pode ser colocada em uma aeronave e verifique se a aeronave
pode levantar vôo ou não. Considere os seguintes critérios:
· O peso de decolagem da aeronave é sempre igual a 500.000 kg;
· O peso de decolagem é composto pela soma do peso do combustível, do peso da carga, do peso dos
passageiros;
· O peso do combustível é a quantidade do combustível (em litros) multiplicada pelo fator 1.5kg/l;
· A quantidade mínima de combustível para que a aeronave decole é de 10000 l;
· O peso da carga é o somatório do peso dos “containers” de cargas em quilogramas.
· O peso dos passageiros é o somatório do peso de cada passageiro e de todos os volumes da sua
bagagem; cada passageiro tem o peso estimado de 70kg e cada volume de bagagem tem o peso
estimado de 10kg.
O algoritmo deve ler o números de containers e a seguir ler o peso de cada container. A seguir devem
ser lidos os dados dos passageiros (número do bilhete, quantidade de bagagens) até que o número do
bilhete seja igual a 0. Devem ser mostrados, a quantidade de passageiros, a quantidade total de volume
de bagagem, o peso dos passageiros, o peso da carga, a quantidade possível de combustível, e uma
mensagem indicando a liberação da decolagem ou não.
'''

def calcular_peso_combustivel_litros(min_combustivel_litros):
    return min_combustivel_litros * 1.5  # Fator de conversão para kg

def verificar_decolagem(peso_decolagem, min_combustivel_kg):
    if min_combustivel_kg >= 10000:
        print("Decolagem liberada!")
    else:
        print("Quantidade insuficiente de combustível. Decolagem não liberada.")

def main():
    num_containers = int(input("Digite o número de containers de carga: "))
    peso_carga = sum([float(input(f"Peso do container {i + 1}: ")) for i in range(num_containers)])

    num_passageiros = 0
    total_bagagem = 0
    peso_passageiros = 0

    bilhete = int(input("Digite o número do bilhete do passageiro (0 para terminar): "))
    while bilhete != 0:
        num_passageiros += 1
        num_bagagens = int(input("Digite a quantidade de bagagens do passageiro: "))
        total_bagagem += num_bagagens
        peso_passageiros += (num_bagagens * 10) + 70  # Peso do passageiro (70kg) + peso de cada bagagem (10kg)
        bilhete = int(input("Digite o número do bilhete do próximo passageiro (0 para terminar): "))

    peso_decolagem = 500000  # Peso de decolagem fixo
    peso_decolagem += peso_carga
    peso_decolagem += peso_passageiros

    min_combustivel_litros = max((10000 - peso_decolagem) / 1.5, 0)  # Garantir que o combustível seja 0 se não houver necessidade
    min_combustivel_kg = min_combustivel_litros * 1.5  # Convertendo litros para kg

    print("\nResultados:")
    print("Quantidade de passageiros:", num_passageiros)
    print("Quantidade total de volume de bagagem:", total_bagagem)
    print("Peso dos passageiros:", peso_passageiros, "kg")
    print("Peso da carga:", peso_carga, "kg")
    print("Quantidade possível de combustível:", min_combustivel_litros, "litros")
    
    verificar_decolagem(peso_decolagem, min_combustivel_kg)


main()
