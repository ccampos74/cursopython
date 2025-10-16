'''from math import factorial
num = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(num)
print('O fatorial de {} é {}'.format(num, f))'''

num = int(input('Digite um número para calcular seu fatorial: '))
cont = num
fat = 1
print('Calculando {}! ='.format(num), end=' ')
while cont > 0:
    print('{}'.format(cont), end=' ')
    print(' x ' if cont > 1 else ' = ', end=' ')
    fat *= cont
    cont -= 1
print('{}'.format(fat))