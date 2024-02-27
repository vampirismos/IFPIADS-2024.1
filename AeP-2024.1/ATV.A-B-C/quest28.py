#28. Leia um número inteiro de horas, calcule e escreva quantas semanas, quantos dias e quantas horas ele corresponde.
#comecei a ficar com preguiça de fazer enfeitadinho....


#Entrada
hrs = int(input("> Digite um número inteiro de horas a ser convertido: "))


#Processamento
weeks = hrs // 168
days = (hrs % 168) // 24
hrs_rest = hrs % 24

#Saída
print(f"> {hrs}h corresponde a: {weeks} semanas, {days} dias e {hrs_rest}hrs.")