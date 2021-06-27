# A tupla é uma sequência imutável

tupla = tuple()
tupla = ()
print(type(tupla))
print(dir(tupla))

tupla = ('um',)
# tupla[0] = 'novo'
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores)
print(cores[0])
print(cores[-1])
print(cores[1:])

# Se existe o elemento dentro da tupla
print(cores.index('amarelo'))

# Quantos elementos existem na tupla
print(cores.count('azul'))

# Tamanho da tupla
print(len(cores))
