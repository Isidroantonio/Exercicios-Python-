# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.


from math import sqrt
from pickle import APPEND

primos = [2, 3, 5, 7, 11]

for n in range(11, 2000):
    r = n % 2 and n % 3 and n % 5 and n % 7 and n % 11
    if r != 0:
        primos.append(n)
print(primos)
