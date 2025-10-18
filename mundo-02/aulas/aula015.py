print('=== Estrutura de Repetição com parada ===')
print('=-'*21)

cont = 0
while cont <= 10: # flag
    print(cont, ' ', end='')
    cont += 1
print('acabou')
print('=-'*21)

n = 0
while n != 999:
    n= int(input('Digite um número: '))
print('=-'*21)

print('Gambiarra')
n = s = 0
while n != 999:
    n =int(input('Digite um número: '))
    s += n
s -= 999 # >>> gambiarra <<<
print(f'A soma vale {s}')
print('=-'*21)

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')
print('=-'*21)

print('F-STRINGS')
nome = 'José'
idade = 33
salario = 987.3
print(f'O {nome} tem {idade} anos e ganha R${salario:.2f}')
print(f'{nome:^20}')
print(f'{nome:-<20}')
print(f'{nome:->20}')
print(f'{nome:-^20}')
print('=-'*21)