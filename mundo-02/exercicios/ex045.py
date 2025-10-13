print('{}JO{}{}KEN{}{}PÔ{}'.format('\033[31m', '\033[m', '\033[33m', '\033[m', '\033[34m', '\033[m'))
from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
comp = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
usr = int(input('Qual é a sua jogada? ')) 
sleep(1) 
print('{}JO{}'.format('\033[31m', '\033[m'))
sleep(1)
print('{}KEN{}'.format('\033[33m', '\033[m'))
sleep(1)
print('{}PÔ!!!{}'.format('\033[34m', '\033[m'))
print('-='*15)
print('O computador jogou {}'.format(itens[comp]))
print('O usuário jogou {}'.format(itens[usr]))
print('-='*15)
if comp == 0: #comp jogou pedra
    if usr == 0:
        print('EMPATE')
    elif usr == 1:
        print('JOGADOR VENCEU!!!')
    elif usr == 2:
        print('COMPUTADOR VENCEU!!!')
    elif usr > 2:
        print('OPÇÃO INVÁLIDA')
elif comp == 1: #comp jogou papel
    if usr == 0:
        print('COMPUTADOR VENCEU!!!')
    elif usr == 1:
        print('EMPATE')
    elif usr == 2:
        print('JOGADOR VENCEU!!!')
    elif usr > 2:
        print('OPÇÃO INVÁLIDA')
elif comp == 2: #comp jogou tesoura
    if usr == 0:
        print('JOGADOR VENCEU!!!')
    elif usr == 1:
        print('COMPUTADOR VENCEU!!!')
    elif usr == 2:
        print('EMPATE')
    elif usr > 2:
        print('OPÇÃO INVÁLIDA')
