print(f'{' LOJAS CCAMPOS ':=^35}')
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] à  vista dinheiro / cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Selecione a opção desejada: '))
if opcao == 1:
    pfinal = preco - (preco * 10 / 100)
elif opcao == 2:
    pfinal = preco - (preco * 5 / 100)
elif opcao == 3:
    pfinal = preco
    vparcela = pfinal / 2
    print('Sua compra será parcelada em duas vezes de R${:.2f} SEM JUROS.'.format(vparcela))
elif opcao == 4:
    parcela = int(input('Quantidade de parcelas: '))
    pfinal = preco + (preco * 20 / 100)
    vparcela = pfinal / parcela
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(parcela, vparcela))
else:
    print('{}OPÇÃO INVÁLIDA DE PAGAMENTO{}'.format('\033[31m', '\033[m'))
    preco = 0
    pfinal = 0
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, pfinal))
