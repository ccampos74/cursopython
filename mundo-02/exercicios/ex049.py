print(f'{' TABUADA 2.0 ':=^23}')
n = int(input('Escolha um número, para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n * c))
