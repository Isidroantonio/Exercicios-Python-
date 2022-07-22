# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o
#  fatorial várias vezes e limitando o fatorial a números inteiros positivos
#  e menores que 16.

from math import factorial

print('-'*30)
print('Fatoração')
print('-'*30)

numInt = int(input('qual número deseja fatorar ?'))

print(factorial(numInt))