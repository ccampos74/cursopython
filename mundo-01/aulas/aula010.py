'''
               ====Condição====
tempo = int(input('Quantos anos tem eu carro? '))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')

             ===Condoção Simplificada===
tempo = int(input('Quantos anos tem eu carro? '))
print('Carro novo' if tempo <=3 else 'Carro velho')
print('--FIM--')
'''

nome = str(input('Qual é o seu nome? '))
if nome == 'Claudio':
    print('Que lindo nome você tem!')
print('Bom dia, {}!'.format(nome))