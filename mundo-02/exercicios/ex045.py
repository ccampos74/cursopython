from random import randint
from time import sleep
print('{}JO{}KEN{}PÔ{} 2.0{}'.format('\033[32m', '\033[33m', '\033[34m', '\033[31m', '\033[m'))
print('''OPÇÕES:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
usr = int(input('Digite sua opção: '))
comp = randint(0, 2)
itens = ('PEDRA', 'PAPEL', 'TESOURA')
print('{}JO{}'.format('\033[32m', '\033[m'))
sleep(1)
print('{}KEN{}'.format('\033[33m', '\033[m'))
sleep(1)
print('{}PÔ!!!{}'.format('\033[34m', '\033[m'))
sleep(1)
if usr <= 2:
    print('-='*12)
    print('Usuário jogou {}'.format(itens[usr]))
    print('Computador jogou {}'.format(itens[comp]))
    print('-='*12)
    if usr == comp:
        print('{}EMPATE{}'.format('\033[33m', '\033[m'))
    elif usr == 0:
        if comp == 1:
            print('{}COMPUTADOR VENCEU!!!{}'.format('\033[36m', '\033[m'))
        elif comp == 2:
            print('{}USUÁRIO VENCEU!!!{}'.format('\033[32m', '\033[m'))
    elif usr == 1:
        if comp == 0:
            print('{}USUÁRIO VENCEU!!!{}'.format('\033[32m', '\033[m'))
        elif comp == 2:
            print('{}COMPUTADOR VENCEU!!!{}'.format('\033[36m', '\033[m'))
    elif usr == 2:
        if comp == 0:
            print('{}COMPUTADOR VENCEU!!!{}'.format('\033[36m', '\033[m'))
        elif comp == 1:
            print('{}USUÁRIO VENCEU!!!{}'.format('\033[32m', '\033[m'))
else:
    print('{}OPÇÃO INVÁLIDA{}'.format('\033[31m', '\033[m'))