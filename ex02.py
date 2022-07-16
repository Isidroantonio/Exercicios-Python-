# Faça um programa que leia um nome de usuário e a sua senha e não aceite a 
# senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando
#  a pedir as informações.

def login():
    nome = input('Digite seu login: ')
    senha = input('Digite sua senha :')
    if nome == senha:
        print('Senha inválida, sua senha deve ser diferente do login.')
        login()
    else:
        print('Bem vindo a Zi Corp!')
login()

