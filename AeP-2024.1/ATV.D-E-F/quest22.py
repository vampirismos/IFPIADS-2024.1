'''
22. Leia a hora do início de um jogo e a hora de fim do jogo (cada hora é composta por 2 variáveis inteiras:
hora e minuto). Calcule e escreva a duração do jogo (horas e minutos), sabendo-se que o tempo
máximo de duração do jogo é de 24 horas e que ele pode iniciar-se em um dia e terminar no dia
seguinte.
'''



def calcular_duracao_jogo(hora_inicio, minuto_inicio, hora_fim, minuto_fim):
    minutos_inicio = hora_inicio * 60 + minuto_inicio
    minutos_fim = hora_fim * 60 + minuto_fim

    duracao_minutos = (minutos_fim - minutos_inicio + 24 * 60) % (24 * 60)

    duracao_horas = duracao_minutos // 60
    duracao_minutos %= 60

    return duracao_horas, duracao_minutos

def main():
    hora_inicio = int(input("Informe a hora de início do jogo: "))
    minuto_inicio = int(input("Informe o minuto de início do jogo: "))
    hora_fim = int(input("Informe a hora de fim do jogo: "))
    minuto_fim = int(input("Informe o minuto de fim do jogo: "))

    duracao_horas, duracao_minutos = calcular_duracao_jogo(hora_inicio, minuto_inicio, hora_fim, minuto_fim)

    print(f"A duração do jogo é de {duracao_horas} horas e {duracao_minutos} minutos.")



main()
