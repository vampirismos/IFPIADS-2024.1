'''
7. Leia um número e, a seguir, leia uma lista de números até achar um igual ao primeiro número lido.
'''

def main():
    numero = int(input('Informe um número ^-^ : '))
    val = None
    while(val!=numero):
        val = int(input('Informe outro número ^-^ : '))

    print("Vocẽ encontrou o número ^-^ !!")

main()