# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o
# fatorial várias vezes e limitando o fatorial a números inteiros positivos
# e menores que 16.

from math import factorial

def fatorial():
    numInt = int(input('qual número deseja fatorar ?'))

    if numInt > 16 or numInt < 0:
        print('Fatorial não permitida, entre com um número entre 1 e 16: ')
        fatorial()
    else:
        print(factorial(numInt))

print('-'*30)
print('Fatoração')
print('-'*30)
fatorial()