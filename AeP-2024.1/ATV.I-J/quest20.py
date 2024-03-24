'''
20. Considere que um carro vai fazer uma viagem entre duas cidades e que a distância a ser percorrida é de
**600 km**. No início da viagem, o carro está com o **tanque cheio (50 litros)**. Durante o percurso foi usado
um aparelho para medir o desempenho do carro, que mostrava, quando acionado, duas informações:
· Distância percorrida desde a última medição;
· Quantidade de litros consumidos para percorrer a distância indicada.
Escreva um algoritmo que **leia** estas informações e escreva:
· se o carro chegou ao seu destino (distância percorrida maior ou igual a 600 km);
· se o carro parou antes de chegar por falta de combustível (consumo igual a 50 litros);
· o consumo em km/l do carro.
'''

def main():

    distancia_percorrida = 0
    litros_percorrido = 0

    while(distancia_percorrida < 600 and litros_percorrido < 50):
        distancia = int(input("Informe distância percorrida: "))
        litros = int(input("Informe litros consumidos: "))
        distancia_percorrida += distancia
        litros_percorrido += litros

    if distancia_percorrida >= 600:
        print("O carro chegou ao seu destino!")
    else:
        print("O carro não chegou ao seu destino.")
        if litros_percorrido >= 50:
            print("Parou por falta de combustível.")
    
    if distancia_percorrida > 0:
        consumo = distancia_percorrida / litros_percorrido
        print(f"Consumo do carro: {consumo:.2f} km/l")

main()


    
        

