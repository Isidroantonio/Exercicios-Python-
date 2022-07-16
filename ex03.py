#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

#enrada de dados
def nome():
    nome = input('Digite seu nome: ')
    tamanho = len(nome)
    if tamanho <= 3:
        print('Nome inválido, digite novamente.')
        nome()
    else:
        return nome

def idade():
    idade = int(input('Digite sua idade: '))
    if idade < 0:
        print('Idade negativa, digite novamente.')
        idade()
    elif idade > 150:
        print('Não tão velho assim poxa, digite novamente.')
        idade()
    else:
        return idade

def salario():
    salario = int(input('Digite seu salário: '))
    if salario <0:
        print('Salário invalido, ta devendo porra ?, Digita de novo.')
        salario()
    else:
        return salario

def sexo():
    sexo = input('Qual seu sexo: ')
    if sexo != 'm' and 'f':
        print('Opção inválida, digite novamente.')
        sexo()
    else: 
        return sexo

def estadocivil():
    ecivil = input('Qual seu estado civil: ')
    if ecivil != 's' and 'c' and 'd' and 'v':
        print('Opção inválida, digite novamente.')
        estadocivil()
    else: 
        return ecivil

nome = nome()
idade = idade()
salario = salario()
sexo = sexo()
civil = estadocivil()

print('''
Nome: {};
Idade: {};
Salário: {};
Sexo: {};
Estado Civil: {}'''.format(nome, idade, salario, sexo, civil))

