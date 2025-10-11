num = int(input('Digite um número de 0 a 9999: '))
print('Analisando o número {}'.format(num))
m = num // 1000
c = (num% 1000) // 100
d = ((num% 1000)% 100) //10
u = (((num% 1000)% 100)% 10)// 1

# u = num // 1 % 10
# d = num // 10 % 10
# c = num // 100 % 10
# m = num // 1000 % 10

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
