sal = float(input('Digite o salário: '))
aum = (sal / 100) * 15
salatual = sal + aum
print('O salário de R${:.2f} com o aumento de 15%, passa a valer R${:.2f}'.format(sal, salatual))
