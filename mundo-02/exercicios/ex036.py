print('\033[44m BANCO CCAMPOS \033[m')
casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
ano = int(input('Qquantos anos de financiamento? '))
prestacao = casa / (ano * 12)
emprestimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(casa, ano, prestacao))
if prestacao > emprestimo:
    print('Empréstimo {}NEGADO{}!'.format('\033[31m', '\033[m'))
else:
    print('Parabéns!, empréstimo pode ser {}CONCEDIDO{}!'.format('\033[32m', '\033[m'))
