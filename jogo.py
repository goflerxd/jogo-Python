#! /usr/bin/python3.8

'''
Jogo de acerta um número - seguencia
Boas Vindas
Sistema sorteia um número
Sistema solicita o nome do jogador
Sistema solicita ao jogador seu palpite
Se errou, informar se para mais ou para menos
Solicitar outro palpite e
informar quantas tentativas ainda restantes
Se acertou, parabenizar e informar o número de 
tentativas utilizadas. 
Número máximo de tentativas = 7
'''

import random
chute = 0
chances = 7
tentativas = 1
jogador = ''

# o sistema fará o sorteio de um número de 1 a 100
numero_secreto = random.randint(1,100)

print('##################################################')
print('######### Bem vindo ao jogo de advinhar ##########')
print('# Você terá sete chances para adivinhar o número #')
print('##################################################')

# programa solicita o nome do jogador
jogador = input('Digite seu nome: ')
print('Chute um número de 1 a 100')

while tentativas <= chances:
     
    chute = int(input('Chute um número: '))
    
    if chute < numero_secreto:
        print('Você errou. É maior, tente novamente!')
        print('Tentativa %d de %d chances.' % (tentativas, chances))
    elif chute > numero_secreto:
        print('Você errou. É menor, tente novamente!')
        print('Tentativa %d de %d chances.' % (tentativas, chances))
    else:
        print()
        print('PARABÉNS!!!!!!!!!!!!!', jogador)
        if tentativas == 1:
            print('Você acertou com %d tentativa.' % tentativas)
        else:
            print('Você acertou com %d tentativas.' % tentativas)
        print()
        tentativas = 7
    
    if tentativas == 6:
        print('Última tentativa', jogador)
        print()
    if tentativas == 7:
        print('######## Fim do Jogo! ########')
        print()
        
    tentativas = tentativas + 1
    
    if tentativas == 8:
        print('O número secreto sorteado foi',numero_secreto,",",jogador)
        print()
              
print('#################################################')
print('####### Volte sempre ao jogo de advinhar ########')
print('#################################################')
input('tecle ENTER para sair') # para não finalizar sem ver o resultado 