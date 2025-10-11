'''
    *frase está sendo usada como variável nos exemplos
    Fatiamento:
    [] o último valor é ignorado
    Análise:
    len() = comprimento
    frase.count(' ') = conta as vezes q um caractere a frase tem
    frase.find('') = encontrar > indica o n⁰ que está o caractere,
    se retornar -1 , não existe
    'palavra' in frase = true e false
    transformação: mudança através de método
    frase.replace('Python', 'Android') = troca Python por Android
    frase.upper() = maiúscula
    frase.lower() = minúuscula
    frase.capitalize() = somente a 1⁰ letra da frase fica maiúscula
    frase.title() = A 1⁰ letra de todas as palavras da frase ficam maiúsculas
    frase.strip() = retira todos os espaços da frente e do fim da frase
    frase.lstrip() = retira os espaços da esquerda
    frase.rstrip() = retira os espaços da direita
    divisão:
    frase.split() = divide a frase pelos espaços, cria uma lista com um índice individual para cada palavra e um n⁰ split tbm iniiciado em 0
    junção:
    ' '.join(frase) = une os elementos com espaço ou símbolo usado entre as aspas
'''

frase = 'Curso em Vídeo Python'
print(frase)
print('='*23)
print(f'{' transformação ':=^17}')
print(frase[3])
print(frase[3:13])
print(frase[:14])
print(frase[13:])
print(frase[1:15:2])
print(f'{' análise ':=^17}')
print(frase.count('o'))
print(len(frase.strip()))
print(frase.replace('Python', 'Android'))
print('Curso' in frase)
print(frase.find('Vídeo'))
print(frase.lower().find('vídeo'))
print(frase.split())
dividido = frase.split()
print(dividido[2])
print(dividido[2] [3])
