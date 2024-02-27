#10. Leia 2 números inteiros, calcule e escreva o quociente e o resto da divisão do 1o pelo 2o.

#Entrada
print("Vamos brincar de divisão! Digite dois números e veja o resultado da divisão entre eles!")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
numb_1 = float(input("Digite o primeiro número: "))
numb_2 = float(input("Digite o segundo número: "))

#Processamento
divisao = numb_1 // numb_2
rest_divi = numb_1 % numb_2

#Saída

print("Sua divisão obteve os seguintes resultados:")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print(f"O quociente da divisão resultou em: {divisao}")
print(f"O resto da divisão resultou em: {rest_divi}")