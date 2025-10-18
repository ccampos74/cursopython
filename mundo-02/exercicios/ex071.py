print('='*29)
print('{:^29}'.format('BANCO CEV'))
print('='*29)
saque = int(input('Que valor você quer sacar? R$'))
valor = saque
nota = 50
contnota = 0
while True:
    if valor >= nota:
        valor -= nota
        contnota += 1
    else:
        if contnota > 0:
            print(f'Total de {contnota} de {nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        contnota = 0
        if valor == 0:
            break
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')