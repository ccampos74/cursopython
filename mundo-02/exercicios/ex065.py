valor = 'S'
num2 = 0
cont = 0
maior = 0
menor = 0
while valor != 'N':
    num = int(input('Digite um número: '))
    valor = str(input('Quer continuar?[S/N] ')).strip()[0].upper()
    soma = num + num2
    num2 =soma
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print('Você digitou {} números e a média foi {}.'.format(cont, soma / cont))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
