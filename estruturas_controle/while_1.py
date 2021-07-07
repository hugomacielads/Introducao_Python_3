from random import randint

numero_infomado = -1
numero_secreto = randint(0, 9)

while numero_infomado != numero_secreto:
    numero_infomado = int(input('Informe o número: '))

print('Número secreto {} foi encontrado!'.format(numero_secreto))
