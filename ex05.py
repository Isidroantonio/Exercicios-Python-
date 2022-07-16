# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de 
# crescimento iniciais. Valide a entrada e permita repetir a operação.

def crescimento():
    paisA = int(input('Qual a população do pais com menos pessoas? \n'))
    paisB = int(input('Qual a população do pais com mais pessoas ?\n'))

    taxaA = float(input('Qual a taxa de crescimento do país A ?\n'))
    taxaB = float(input('Qual a taxa de crescimento do país B ?\n'))

    anos = 0
    while paisA < paisB:
        paisA = paisA + (paisA * taxaA)
        paisB = paisB + (paisB * taxaB)
        anos = anos + 1
    print('Serão necessários {} anos para a população do PAIS A igualar ou ultrapassar o PAIS B.'.format(anos))

def descisao():
    resp = input('Deseja calcular novamente? (s ou n)\n')
    if resp == 's':
        crescimento()
    elif resp == 'n':
        print('Finalizando.')
    else:
        print('Resposta invalida.')
        descisao()

crescimento()
descisao()