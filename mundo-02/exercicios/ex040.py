n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, m))
if m >= 7:
    print('O aluno está {}APROVADO{}.'.format('\033[32m', '\033[m'))
elif m >= 5:
    print('O aluno está em {}RECUPERAÇÃO{}.'.format('\033[33m', '\033[m'))
elif m >= 0:
    print('O aluno está {}REPROVADO{}.'.format('\033[31m', '\033[m'))
