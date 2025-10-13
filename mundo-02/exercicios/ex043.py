print(f'{' Calculadora IMC ':=^27}')
peso = float(input('Qual o seu peso? (Kg)'))
altura = float(input('Qual a sua altura? (m)'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal.')
elif imc < 25:
    print('Parabéns, vocẽ está na faixa de PESO NORMAL.')
elif imc < 30:
    print('Você está em SOBREPESO!')
elif imc < 40:
    print('Vocẽ está em OBESIDADE')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
