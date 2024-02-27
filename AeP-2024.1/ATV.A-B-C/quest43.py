'''
43. Um sistema de equações lineares do tipo: 
ax + by = c
dx + ey = f
pode ser resolvido segundo mostrado abaixo: 
x=(ce-bf)/(ae-bd)
y=(af-cd)/(ae-bd)
'''

#Entrada
val_a = float(input("Digite o coeficiente a: "))
val_b = float(input("Digite o coeficiente b: "))
val_c = float(input("Digite o coeficiente c: "))
val_d = float(input("Digite o coeficiente d: "))
val_e = float(input("Digite o coeficiente e: "))
val_f = float(input("Digite o coeficiente f: "))

#Processamento
denominador = val_a* val_e - val_b * val_d
val_x = (val_c * val_e - val_b * val_f) / denominador
val_y = (val_a * val_f - val_c * val_d) / denominador

#Saída
print(f"As soluções para o sistema de equações são: x = {val_x: .2f}, y = {val_y: .2f}.")
