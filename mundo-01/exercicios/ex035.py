print('\033[33m-=\033[m'*12)
print('\033[34mAnalisador de Triângulos\033[]')
print('\033[33m-=\033[m'*12)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and a + c > b and b + c > a:
    print('Os seguimentos acima \033[32mPODEM FORMAR\033[m um triângulo')
else:
    print('Os segmentos acima \033[31mNÃO PODEM FORMAR\033[m um triângulo')
