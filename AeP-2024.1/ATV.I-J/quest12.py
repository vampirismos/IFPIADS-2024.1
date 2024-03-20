'''
12. Leia vários códigos do jogador (1 ou 2) que ganhou o ponto, em uma partida de pingue-pongue, e
responda quem ganha a partida. A partida chega ao final se:
· Um dos jogadores chega a 21 pontos e a diferença de pontos entre os jogadores é maior ou igual a 2.
· Se a primeira não for atendida, ganha aquele que, com mais de 21 pontos, consiga colocar uma
diferença de 2 pontos sobre o adversário.
'''

def verificar_vencedor(pontos_jogador1, pontos_jogador2):
    if pontos_jogador1 >= 21 and pontos_jogador1 - pontos_jogador2 >= 2:
        return 1
    elif pontos_jogador2 >= 21 and pontos_jogador2 - pontos_jogador1 >= 2:
        return 2
    else:
        return 0

def partida_pingue_pongue():
    pontos_jogador1 = 0
    pontos_jogador2 = 0

    while True:
        codigo_jogador = int(input("Digite o código do jogador que ganhou o ponto (1 ou 2), ou 0 para encerrar a partida: "))
        
        if codigo_jogador == 0:
            break
        
        if codigo_jogador == 1:
            pontos_jogador1 += 1
        elif codigo_jogador == 2:
            pontos_jogador2 += 1
        else:
            print("Código inválido. Por favor, digite 1, 2 ou 0 para encerrar a partida.")
            continue
        
        vencedor = verificar_vencedor(pontos_jogador1, pontos_jogador2)
        if vencedor != 0:
            print(f"O jogador {vencedor} venceu a partida!")
            break

partida_pingue_pongue()
