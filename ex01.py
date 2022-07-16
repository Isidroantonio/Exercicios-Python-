# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o 
# valor seja inválido e continue pedindo até que o usuário informe um valor válido.

def notas():
    nota = int(input('Digie uma nota entre 0 e 10: '))
    if nota < 0:
        print('Nota negativa não existe, Digite novamente!')
        notas()
    elif nota > 10:
        print('Nota ultrapassa a maxíma aceitavel, digite novamente')
        notas()
    else:
        print('Sua nota é {}'.format(nota))
notas()