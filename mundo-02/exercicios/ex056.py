somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomehomem =''
totalm20 = 0

for c in range(1, 5):
    print('===== {}⁰ PESSOA ====='.format(c))
    nome = str(input('Nome:'))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))

    somaidade += idade

    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomehomem = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomehomem = nome

    if sexo in 'Ff' and idade < 20:
        totalm20 += 1

mediaidade = somaidade /4
print('A média de idade do grupo é de {:.1f} anos.'.format(mediaidade))
print('O homem  mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomehomem))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totalm20))  