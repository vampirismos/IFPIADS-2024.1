'''
25. Verifique a validade de uma senha fornecida pelo usuário. A senha é 1234. O algoritmo deve escrever
uma mensagem de permissão de acesso ou não.
'''

def verificacao_senha(senha):
    if senha == 1234:
       return "Acesso concedido."
    else:
        return "Intruso. Processo de exterminação iniciado."
    

def main():
    senha = int(input("Digite a senha: "))

    resultado = verificacao_senha(senha)
    print(resultado)



main()