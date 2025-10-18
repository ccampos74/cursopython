print('\033[33m-=\033[m'*14)
print('\033[33m  VAMOS JOGAR PAR OU ÍMPAR  \033[m')
print('\033[33m-=\033[m'*14)
from random import randint
cont = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(1, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Jogador escolheu {jogador} e o Computador {computador}. Total de {total},',end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {cont} vezes.')
