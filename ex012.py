preco = float(input('Digite o preço do produto: R$'))
desc = (preco / 100) * 5
novopreco = preco - desc
print('O produto que custava R${:.2f}, com o desconto de 5% passa a custar R${:.2f}'.format(preco, novopreco))
#preco - (preco * 5 / 100)
