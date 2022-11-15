# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro 
# entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. 

import math

def tabuadas():

    print('-'*30)
    print('Gerador de Tabuadas.')
    print('-'*30)

    tabuadaValor = int(input('Qual tabuada deseja calcular: '))
    valorMax = int(input('Qual valor maxímo deseja calcular da tabuada {}: '.format(tabuadaValor)))
    for i in range(1, valorMax+1):
        print(tabuadaValor, 'x', i, '=', tabuadaValor*i)
    
tabuadas()
        
        