par = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}⁰ número: '.format(c)))
    if num % 2 == 0:
        par = par + num
        cont = cont + 1
print('Foram {} números pares e a soma deles é {}'.format(cont, par))
