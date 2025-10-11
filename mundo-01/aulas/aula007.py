'''
Operadores aritméticos
+ adição 5 + 2 == 7
- subtração 5 - 2 == 3
* multiplicação 5 * 2 == 10
/ divisão 5 / 2 == 2.5
** potência 5² == 25
// divisão inteira 5 // 2 == 2
% resto da divisão 5 % 2 == 1
número ** (1/2) raiz quadrada

Ordem de precedência
1 ()
2 **
3 * / // %
4 + -
'''

nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {} \nA multiplicação é {} \nA divisão é {:.3f}'.format(s, m, d))
print('A divisão inteira é {} \nA potência é {}'.format(di, e))
