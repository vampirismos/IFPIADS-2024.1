'''
19. Em um frigorífico, cada boi traz em seu pescoço um cartão contendo o seu n.o de identificação e seu
peso. Escreva um algoritmo que leia um conjunto de cartões e escreva o n.o de identificação e o peso do
boi mais magro e do boi mais gordo. (Flag: n.o identificação=0)
'''



def main():
    n_mais_gordo = ""
    peso_mais_gordo = 0

    n_mais_magro = ""
    peso_mais_magro = float('inf')
    
    n_identificacao = int(input("Nº de identificação (ou 0 para encerrar): "))   
    
    while n_identificacao != 0:
        peso = float(input("Peso do boi (em quilogramas): "))
        
        if peso < peso_mais_magro:
            n_mais_magro = n_identificacao
            peso_mais_magro = peso
        
        if peso > peso_mais_gordo:
            n_mais_gordo = n_identificacao
            peso_mais_gordo = peso
        
        n_identificacao = int(input("Nº de identificação (ou 0 para encerrar): "))  

    
    print("\nPeso do boi mais magro:")
    print(f"Nº de identificação: {n_mais_magro}")
    print(f"Peso: {peso_mais_magro} quilogramas")
    
    print("\nPeso do boi mais gordo:")
    print(f"Nº de identificação: {n_mais_gordo}")
    print(f"Peso: {peso_mais_gordo} quilogramas")

main()

