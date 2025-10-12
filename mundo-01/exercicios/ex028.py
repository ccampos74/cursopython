velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('\033[31mMULTADO! Você excedeu o limite permitido de 80Km/h.\nVocê deve pagar uma multa de\033[31m \033[33mR${:.2f}\033[m'.format(multa))
print('\033[33mTenha um bom dia! Dirija com segurança!\033[m')

