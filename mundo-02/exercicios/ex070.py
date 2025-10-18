print('-'*27)
print('    LOJAS SUPER BARATÃO    ')
print('-'*27)
total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1

    total += preco

    if preco > 1000:
        totmil += 1

    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    '''else: (simplificado no bloco acima)
        if preco < menor:
            menor = preco
            barato = produto'''

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).upper()[0].strip()
    if opcao == 'N':
        break
print(f'O total de compra foi R${total:.2f}')
print(f'Temos {totmil} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi o(a) {barato} que custa R${menor:.2f}')
print('FIM DO PROGRAMA')
