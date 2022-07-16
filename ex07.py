# Faça um programa que leia 5 números e informe o maior número.

numeros = []

for i in range(0, 5):
    num = int(input('Digite um número: '))
    numeros.append(num)

print(numeros)

print(max(numeros))

