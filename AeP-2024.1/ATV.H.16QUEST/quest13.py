'''
13. Faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a) "Telefonou para a vítima ?"
b) "Esteve no local do crime ?"
c) "Mora perto da vítima ?"
d) "Devia para a vítima ?"
e) "Já trabalhou com a vítima ?"
O algoritmo deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa
responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como
"Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''

def main():

    resposta_a = str(input("Telefonou para a vítima? (sim/não): ")).lower()
    resposta_b = str(input("Esteve no local do crime? (sim/não): ")).lower()
    resposta_c = str(input("Mora perto da vítima? (sim/não): ")).lower()
    resposta_d = str(input("Devia para a vítima? (sim/não): ")).lower()
    resposta_e = str(input("Já trabalhou com a vítima? (sim/não): ")).lower()
    
    c = 0
    interrogado = 'hhhhh'
    if(resposta_a == "sim"):
        c +=1
    if(resposta_b == "sim"):
        c +=1
    if(resposta_c == "sim"):
        c +=1
    if(resposta_d == "sim"):
        c +=1
    if(resposta_e == "sim"):
        c +=1

    if (c==2):
        interrogado = "Suspeito"
    elif (c==4 or c==3):
        interrogado = "Cúmplice"
    elif (c==5):
        interrogado = "Culpado"
    else:
        interrogado = "Inocente"

    
    print(f"O interrogado é {interrogado}")


main()