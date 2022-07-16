# Faça um programa que receba dois números inteiros e gere os números inteiros que estão 
# no intervalo compreendido por eles.

num1 = int(input('Digite um número inteiro: \n'))
num2 = int(input('Digite outro número iteiro: \n'))
soma = 0

if num1 > num2:
    for i in range(num2+1, num1):
        print(i)
        soma = soma + i
elif num1 < num2:
    for i in range(num1+1, num2):
        print(i)
        soma = soma + i
else:
    print('Números iguais.')
