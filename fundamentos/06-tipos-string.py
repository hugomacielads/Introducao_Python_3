dir(str)
nome = 'Hugo Cesar'
print(nome)
print(nome[0])

# A string é imutável, podemos gerar uma nova mas não alterar a primeira
# nome[0] = 'P'

# 'marca d'água'
print("Dias D'Ávila" == 'Dias D\'Ávila')
texto = 'Texto entre apóstrofos pode ter "aspas"'
print(texto)

doc = """ Texto com múltiplas
... linhas
"""
print(doc)

# \n (quebra de linha) e \t (espaçamento tab)

# Acesso as posições
nome = 'Ana Paula'
print(nome[0])
print(nome[6])
print(nome[-3])
print(nome[4:])
print(nome[-5:])
print(nome[:3])
print(nome[2:5])

# step (passo)
numeros = '1234567890'
print(numeros)
print(numeros[::])
print(numeros[::2])
print(numeros[1::2])

# Inverter strings
print(numeros[::-2])
print(nome[::-1])

frase = 'Python é uma linguagem excelente'
print('py' in frase)
print('ing' in frase)
print(len(frase))
print('py' in frase.lower())
frase = frase.upper()
print(frase)

print(frase.split('A'))

# Métodos Mágicos (Magic Methods)

a = '123'
b = ' de Oliveira 4'
print(a + b)
a.__add__(b)

print(dir(str))
