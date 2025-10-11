from math import sin, cos, tan, radians
ang = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, cosseno))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, tangente))
