salario = float(input('Qual é o salário do funcionário? '))
if salario >= 1250:
    aumento = salario + (salario / 100) * 10
else:
    aumento = salario + (salario / 100) * 15
print('Quem recebia R${:.2f} passa a receber R${:.2f}'.format(salario, aumento))
