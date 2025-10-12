from random import randint
from time import sleep
computador = randint(0, 5) # faz o computador "PENSAR"
print('\033[34m-=-\033[m'*20)
print("\033[33mVou pensar em um número de 0 a 5, tente adivinhar.\033[m")
print('\033[34m-=-\033[m'*20)
usuario = int(input('Digite seu palpite: '))
print('PROCESSANDO...')
sleep(3)
print('Computador escolheu {}'.format(computador))
print('Você escolheu {}'.format(usuario))
if usuario == computador:
    print('Parabéns! Você venceu!')
else:
    print('Você perdeu! Tente novamente.')
    