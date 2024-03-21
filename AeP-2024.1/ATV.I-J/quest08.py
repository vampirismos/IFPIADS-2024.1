'''
8. Leia um numero X e, a seguir, leia e escreva uma lista de números com o término da lista ocorrendo
quando a soma de dois números consecutivos da lista for igual a X.
'''

def ler_lista_numeros(soma_alvo):
    lista_numeros = []
    while True:
        numero = int(input("Digite um número (digite 0 para terminar): "))
        if numero == 0:
            break
        lista_numeros.append(numero)
        if len(lista_numeros) >= 2:
            if lista_numeros[-1] + lista_numeros[-2] == soma_alvo:
                break
    return lista_numeros

def main():
    soma_alvo = int(input("Digite o número alvo de soma: "))
    lista = ler_lista_numeros(soma_alvo)
    print("Lista de números:", lista)


main()
