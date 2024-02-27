#6. Leia uma velocidade em km/h, calcule e escreva esta velocidade em m/s. (Vm/s = Vkm/h / 3.6)


#Entrada
print('>>>Bem vindo ao conversor de velocidade de Km/h para m/s ! <<<')
print("-------------------------------------------------------------")
vel_kmh = float(input("> Por favor, insira a velocidade em Km/h a ser convertida: "))

#Processamento
vel_ms = vel_kmh / 3.6

#Saída
print("-------------------------------------------------")
print(f"> O resultado de sua conversão é igual a:{vel_ms: .0f}")