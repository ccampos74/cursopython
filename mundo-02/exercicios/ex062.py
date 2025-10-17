print('=== Gerador de PA 3.0 ===')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
opcao = 10
total = 0
while opcao != 0:
    total += opcao
    while cont <= total:
        print('{} ➞'.format(termo), end=' ')
        termo += razao
        cont += 1
    print('PAUSA')
    opcao = int(input('Quantos termos você quer mostrar a mais? '))
print('progressão finalizada com {} termos mostrados.'.format(total))
