# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa capaz de gerar a série até o n−ésimo termo.

print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)

termoAlvo = int(input('Qual seria o termo que deseja chegar? '))

t1 = 0
t2 = 1
print('{} -> {}'.format(t1,t2), end=' ')
cont = 3
while cont <= termoAlvo:
    t3 = t1 + t2
    print('-> {}'.format(t3), end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM!')
    
