n1 = int(input('Digite o 1⁰ valor: '))
n2 = int(input('Digite o 2⁰ valor: '))
opcao = 0
while opcao != 5:
    print('''=== Menu ===
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    opcao = int(input('Digite sua opção: '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma de {} + {} = {}'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O produto de {} x {} = {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {}, omaior é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Digite o 1⁰ valor: '))
        n2 = int(input('Digite o 2⁰ valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida, tente novamente!')
    print('-=' * 10)
print('FIM DO PROGRAMA')
