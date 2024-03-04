'''
12. Leia um número e escreva se o número é inteiro ou decimal.
'''

def main():
    num = float(input("Informe um número: "))
    if(num%1 == 0):
        print(f'O número {num} é inteiro')
    else:
        print(f'O número {num} é decimal')

main()