km = float(input('Qual a distãncia da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}Km'.format(km))
if km <= 200:
    preco = km * 0.50
else:
    preco = km * 0.45
print('E o preço de sua passagem será de R${:.2f}'.format(preco))
