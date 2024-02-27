#1. Leia uma velocidade em m/s, calcule e escreva esta velocidade em km/h. (Vkm/h = Vm/s * 3.6)


#Entrada
print('>>>Bem vindo ao conversor de velocidade de m/s para Km/h ! <<<')
print("-------------------------------------------------------------")
vel_ms = int(input("> Por favor, insira a velocidade em m/s a ser convertida: "))

#Processamento
vel_kmh = vel_ms * 3.6

#Saída
print("-------------------------------------------------")
print(f"> O resultado de sua conversão é igual a:{vel_kmh: .0f}")

