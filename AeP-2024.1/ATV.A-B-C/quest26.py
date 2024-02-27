#26. Leia um número inteiro de dias, calcule e escreva quantas semanas e quantos dias ele corresponde.

#Entrada
print('Precisa saber quantas semanas e dias equivalem a uma determinada quantidade de dias? Posso ajudar!')
val_dias = int(input("Informe a determinada quantidade de dias: "))

#Processamento
val_sem = val_dias // 7
dias_rest = val_dias % 7

#Saída
print(f"{val_dias} corresponde a: {val_sem} semanas e {dias_rest} dias.")