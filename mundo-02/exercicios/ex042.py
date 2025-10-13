print(f'{' Analisando Triângulos v2.0 ':=^38}')
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    if s1 == s2 == s3:
        tipo = 'EQUILÁTERO'
    elif s1 == s2 != s3 or s1 == s3 != s2 or s2 == s3 !=s1:
        tipo = 'ISÓCELOS'
    elif s1 != s2 != s3:
        tipo = 'ESCALENO'
    print('Os segmentos acima PODEM FORMAR um triângulo {}!'.format(tipo))
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triâgulo!')
