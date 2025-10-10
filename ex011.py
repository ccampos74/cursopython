largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
parede = largura * altura
tinta = parede / 2
print('Uma área com {} metros de largura e {} metros de altura, é igual a {}m²'.format(largura, altura, parede))
print('Para pintar a área, será gosto {} litro(s) de tinta.'.format(tinta))