print('-='*13)
print(' JOGO DE ADIVINHAÇÃO 2.0 ')
print('-='*13)
from random import randint
from time import sleep
comp = randint(0, 10)
sleep(1)
print('Sou seu computador...')
sleep(1)
print('Acabei de pensar em um número entre 0 a 10.')
sleep(1)
print('Será que consegue adivinhar qual foi?')
sleep(1)
cont = 1
palpite = int(input('Qual é o seu palpite? '))
while palpite != comp:
    cont += 1
    if palpite > comp:
        print('Menos...Tente mais uma vez!')
    if palpite < comp:
        print('Mais...Tente novamente!')
    palpite = int(input('Qual é o seu palpite? '))
print('Parabéns!!! Acertou com {} tentativas.'.format(cont))
