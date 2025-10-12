from random import randint
computador = randint(0, 5) # faz o computador "PENSAR"
print('-=-'*20)
print("Vou pensar em um número de 0 a 5, tente adivinhar.")
print('-=-'*20)
usuario = int(input('Digite seu palpite: '))
print('Computador escolheu {}'.format(computador))
print('Você escolheu {}'.format(usuario))
if usuario == computador:
    print('Parabéns! Você venceu!')
else:
    print('Você perdeu! Tente novamente.')