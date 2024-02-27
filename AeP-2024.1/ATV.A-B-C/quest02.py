#2. Leia um valor em horas e um valor em minutos, calcule e escreva o equivalente em minutos.


#Entrada
print(">>>Seja bem-vindo ao conversor de horas para minutos!<<<")
print('........................................................')
valor_hrs = int(input("> Por favor insira o valor em HORAS a ser convertido para MINUTOS: "))

#Processamento
valor_min = valor_hrs * 60

#Saída
print('...........................................................')
print(f"> O resultado de sua conversão é igual a: {valor_min: .0f} minutos.")
