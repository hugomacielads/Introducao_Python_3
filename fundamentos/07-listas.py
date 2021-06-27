# A lista é uma estrutura de dados móvel,
# não necessitando de uma nova atribuiçao

lista = []
print(type(lista))
dir(lista)

print(len(lista))

lista.append(1)
lista.append(2)
print(lista)

print(len(lista))

nova_lista = [1, 5, 'Ana', 'Bia']
print(nova_lista)
nova_lista.remove(5)
print(nova_lista)
nova_lista.reverse()
print(nova_lista)

print('Aula 2 -------------------------')

lista = [1, 5, 'Rebeca', 'Guilherme', 3.1415]
print(lista)
print(lista.index('Guilherme'))
# lista.index(42)
print(lista[2])
print(1 in lista)
print('Pedro' not in lista)
print(lista[-1])
print(lista[-5])

print('Aula 3 -----------------------------')

lista = ['Ana', 'Lia', 'Rui', 'Paulo', 'Dani']
print(lista)
print(lista[1:3])
print(lista[1:-1])
print(lista[1:])
print(lista[:-1])
print(lista[::2])
print(lista[::-1])
del lista[2]
print(lista)
del lista[1:]
print(lista)
