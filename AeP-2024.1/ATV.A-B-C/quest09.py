#9. Leia 2 números (A, B) e escreva-os em ordem inversa (B, A).

#Entrada
print("Bem-vindo ao seu invertedor de ordem de números!")
num_a = float(input('Insira o primeiro número da ordem: '))
num_b = float(input("Insira o segundo número da ordem: "))

#Processamento
num_a, num_b = num_b, num_a

#Saída
print(f"A ordem dos números foi invertida. Confira o seguinte resultado: {num_a}, {num_b}")