print('-'*23)
print('  CADASTRO DE PESSOAS  ')
print('-'*23)
maioridade = homem = mulher = 0
while True:
    idade = int(input('Idade: '))
    if idade > 18:
        maioridade += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]')).upper()[0].strip()
        if sexo == 'M':
            homem += 1
        if sexo == 'F' and idade < 20:
            mulher += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N]: ')).upper()[0].strip()
    if opcao == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maioridade}')
print(f'Homens cadastrados: {homem}')   
print(f'Mulheres menores de 20 anos: {mulher}')
