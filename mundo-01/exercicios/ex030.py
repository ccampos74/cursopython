num = int(input('\033[35mMe diga um número qualquer: \033[m'))
if num % 2 == 0:
    print('O número {} é \033[34mPAR\033[m'.format(num))
else:
    print('O nḿero {} é \033[34mÍMPAR\033[m'.format(num))
