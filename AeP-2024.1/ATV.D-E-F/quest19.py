'''
19. Leia a altura (em metros) e peso (em Kg) de uma pessoa, 
em seguida calcule o índice de massa corpórea
(IMC = peso / altura2). Ao final, escreva se a pessoa está 
com peso normal (IMC abaixo de 25), obeso
(IMC entre 25 e 30) ou obesidade mórbida (IMC acima de 30).
'''


def calculo_imc(massa,altura):
    imc = massa / altura**2
    return imc

def verificacao_imc(imc):
    if imc >= 18.5 and imc <= 25:
       return "Você está na faixa de peso recomendada."
    else:
        return "Você não está na faixa de peso recomendada."
    

def classificacao_imc(massa,altura):
    imc = massa / altura**2

    if imc <= 17 and imc <= 18.49:
        return "Abaixo do peso."
    elif imc >= 18.5 and imc <= 25:
        return "Peso normal."
    else:
        return "Acima do peso."


def main():
    massa = float(input("Por favor, informe seu peso em Kg: "))
    altura = float(input("Por fim, informe sua altura em metros: "))
    
    resultado_imc = calculo_imc(massa, altura)
    tipo_imc = classificacao_imc(massa, altura)
    print (f'Seu IMC é {resultado_imc: .2f} e ele se classifica como: {tipo_imc}.')


main()