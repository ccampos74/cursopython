sal = float(input('Digite o salário: R$'))
aum = (sal / 100) * 15
salatual = sal + aum
print('O salário de R${:.2f} com o aumento de 15%, passa a valer R${:.2f}'.format(sal, salatual))
#sal + (sal * 15 / 100)