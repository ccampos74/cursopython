from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}⁰ pessoa nasceu? '.format(c)))
    if atual - ano >= 21:
        maior += 1
    else:
        menor += 1
print('Maior de idade: {} pessoa(s)\nMenor de idade: {} pessoa(s)'.format(maior, menor))
