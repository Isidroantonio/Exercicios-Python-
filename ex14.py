# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de 
# números pares e a quantidade de números impares.

print('-'*30)
print('Par ou impar?')
print('-'*30)

par = 0
impar = 0


for i in range(0, 10):
    num = int(input('Entre com os números: \n'))
    filtro = num % 2
    if filtro == 0:
        par = par + 1
    else:
        impar = impar + 1

print('A quantidade de numeros pares é de {} e a quantidade de números impares é de {}.'.format(par, impar))
