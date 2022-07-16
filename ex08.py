#Faça um programa que leia 5 números e informe a soma e a média dos números.

print('-'*30)
print('Soma e média de números.')
print('-'*30)

lista = []

for i in range(0, 5):
    num = int(input('Digite um número: \n'))
    lista.append(num)
    soma = sum(lista)
    media = soma/5

print('A soma entre os números indicados é de {}.'.format(soma))
print('A média entre os números indicados é de {}.'.format(media))