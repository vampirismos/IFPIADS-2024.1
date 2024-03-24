'''
17. Em um concurso de beleza, cada candidata tem um cartão contendo nome, altura e peso. Escreva um
algoritmo que leia um conjunto de cartões e escreva o nome e a altura da candidata mais alta e da mais
baixa; o nome e o peso da candidata mais magra e da mais gorda. (Flag: nome = 'FIM').
'''

def main():
    nome_mais_alta = ""
    altura_mais_alta = 0
    
    nome_mais_baixa = ""
    altura_mais_baixa = float('inf')
    
    nome_mais_magra = ""
    peso_mais_magra = float('inf')
    
    nome_mais_gorda = ""
    peso_mais_gorda = 0
    
    while True:
        nome = input("Digite o nome da candidata (ou 'FIM' para encerrar): ")
        if nome == 'FIM':
            break
        
        altura = float(input("Digite a altura da candidata (em metros): "))
        peso = float(input("Digite o peso da candidata (em quilogramas): "))
        
        if altura > altura_mais_alta:
            nome_mais_alta = nome
            altura_mais_alta = altura
        
        if altura < altura_mais_baixa:
            nome_mais_baixa = nome
            altura_mais_baixa = altura
        
        if peso < peso_mais_magra:
            nome_mais_magra = nome
            peso_mais_magra = peso
        
        if peso > peso_mais_gorda:
            nome_mais_gorda = nome
            peso_mais_gorda = peso
    
    print("\nCandidata mais alta:")
    print(f"Nome: {nome_mais_alta}")
    print(f"Altura: {altura_mais_alta} metros")
    
    print("\nCandidata mais baixa:")
    print(f"Nome: {nome_mais_baixa}")
    print(f"Altura: {altura_mais_baixa} metros")
    
    print("\nCandidata mais magra:")
    print(f"Nome: {nome_mais_magra}")
    print(f"Peso: {peso_mais_magra} quilogramas")
    
    print("\nCandidata mais gorda:")
    print(f"Nome: {nome_mais_gorda}")
    print(f"Peso: {peso_mais_gorda} quilogramas")


main()


     