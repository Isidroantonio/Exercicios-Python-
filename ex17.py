# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
#  Ex.: 5!=5.4.3.2.1=120

from math import factorial

print('-'*30)
print('Fatoração')
print('-'*30)

numInt = int(input('qual número deseja fatorar ?'))

print(factorial(numInt))