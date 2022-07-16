# Faça um programa que, dado um conjunto de N números, determine o menor valor, 
# o maior valor e a soma dos valores.

conjunto = []

somaConjunto = 0

for i in range(1, 10):
    num = int(input('entre com valores: '))
    conjunto.append(num)
    somaConjunto = somaConjunto + num

print(conjunto)
print(min(conjunto))
print(max(conjunto))
print(somaConjunto)
