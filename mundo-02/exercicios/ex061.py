print('=== Progressão Aritimética 2.0 ===')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} ➞'.format(termo), end=' ')
    termo += razao
    cont += 1
print('FIM')
