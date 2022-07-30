def multiplica(a, b):
    return a * b

cont = 0

investido = multiplica(163, cont)

for i in range(0, 20000, 163):
    print('O valor investido é de {}'.format(i))
    cont += 1
    print('O valor recebido em dividendos é de {:5.2f}'.format(cont * 3.3))
    print('Com isso voce terá {} cotas do FII.'.format(cont))
    print('-'*30)


