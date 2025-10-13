from datetime import date
nascer = int(input('Ano de nascimento: '))
ano = date.today().year
idade = ano - nascer
print('Quem nasceu em {} tem {} anos em {}.'.format(nascer, idade, ano))
if idade < 18:
    alista = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(alista))
    print('Seu alistamento será em {}.'.format(ano + alista))
elif idade > 18:
    alista = idade - 18
    print('Vocẽ já deveria ter se alistado há {} anos'.format(alista))
    print('Seu alistamento foi em {}'.format(ano - alista))
else:
    print('Você tem que se alistar IMEDIATAMENTE!')
