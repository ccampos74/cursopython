mult = 0
prod = 0
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('\033[33m-=\033[m'*20)
    if num < 0:
        break
    while True:
        if mult == 10:
            break
        mult += 1
        prod = num * mult
        print(f'{num} X {mult:2} = {prod:2}')
    print('\033[33m-=\033[m'*20)
    mult = 0
print('\033[31mPROGRAMA TABUADA ENCERRADO! VOLTE SEMPRE!\033[m')

'''
while True:
    n = int(input(' Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-'*30)
print('PROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE!')
'''