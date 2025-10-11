'''
    import: importa toda a biblioteca
    from biblioteca import módulo: somente o módulo
'''

#import math
from math import sqrt
num = int(input('Digite um número: '))
#raiz = math.sqrt(num)
raiz = sqrt(num)
print('A raíz de {} é igual a {:.2f}'.format(num, raiz))
print('='*40)
