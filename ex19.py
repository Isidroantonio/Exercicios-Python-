# Faça um programa que, dado um conjunto de N números, determine o menor valor, 
# o maior valor e a soma dos valores.

# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

conjunto = []
count = 0
somaConjunto = 0

quantidade = int(input('quantos numeros deseja: '))
while quantidade != count:
    num = int(input('entre com valores: '))

    while num > 1000 or num < 0:
        num = int(input('Número inválido, entre novamente: '))
    conjunto.append(num)
    somaConjunto = somaConjunto + num
    count += 1

print(conjunto)
print(min(conjunto))
print(max(conjunto))
print(somaConjunto)
