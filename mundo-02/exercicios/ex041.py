from datetime import date
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    cat = 'MIRIM'
elif idade <= 14:
    cat = 'INFANTIL'
elif idade <= 19:
    cat = 'JUNIOR'
elif idade <= 25:
    cat = 'SÊNIOR'
else:
    cat = 'MASTER'
print('Categoria: {}'.format(cat))
