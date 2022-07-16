# Altere o programa anterior para mostrar no final a soma dos números.

num1 = int(input('Digite um número inteiro: \n'))
num2 = int(input('Digite outro número iteiro: \n'))
soma = 0
print('-'*30)

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

print('-'*30)
print('A soma dos números entre o intervalo de {} e {} é {}.'.format(num1, num2, soma))