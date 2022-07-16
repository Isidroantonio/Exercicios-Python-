# Faça um programa que peça dois números, base e expoente, calcule e mostre o 
# primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

print('-'*30)
print('Potenciação.')
print('-'*30)

base = int(input('Entre com o valor da base: '))
expoente = int(input('Entre com o valor do expoente: '))

res = base ** expoente
print('O valor da operação é {}.'.format(res))