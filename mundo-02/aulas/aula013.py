print('Laços de Repetição')
for c in range(0, 6):
    print('oi')
print('fim')
print('='*15)
for c in range(0, 6):
    print(c)
print('fim')
print('='*15)
for c in range(6, 0, -1):
    print(c)
print('fim')
print('='*15)
for c in range(0, 7, 2):
    print(c)
print('fim')
print('='*15)
n = int(input('Digite um número: '))
for c in range(0, n):
    print(c)
print('fim')
print('='*15)
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('fim')
print('='*15)
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('fim')
print('='*15)
for c in range(0, 3):
    n = int(input('Digite um número: '))
print('fim')
print('='*15)
s = 0
for c in range(0, 4):
    n =int(input('Digite um valor: '))
    s += n
print('A soma de toodos os valores é igual a {}'.format(s))
