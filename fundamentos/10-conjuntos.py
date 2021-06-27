a = {1, 2, 3}
print(type(a))
a = set('Huuuugo')
print(a)
print('g' in a, 4 not in a)
print({1, 2, 3} == {3, 2, 1, 3})

# Operações
# União, intersecção e update
c1 = {1, 2}
c2 = {2, 3}
print(c1.union(c2))
print(c1.intersection(c2))
print(c1.update(c2))
print(c1)
