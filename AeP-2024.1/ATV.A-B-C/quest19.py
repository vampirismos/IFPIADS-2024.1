#19. Leia o valor do raio de uma esfera, calcule e escreva seu volume. (v = (4 * p * r3) / 3) (p = 3,14)

#Entrada
print("Vamos calcular o volume de uma esfera!")
print("--------------------------------------")
raio = float(input("> Por favor, informe o valor do raio da esfera: "))

#Processamento
volume = (4 * 3.14 * raio**3) / 3

#Saída
print(f"> O volume dessa esfera é aproximadamente: {volume: .2f}.")