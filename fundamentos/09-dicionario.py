pessoa = {'nome': 'Prof Ana', 'idade': 38, 'cursos': ['Inglês', 'Português']}
print(type(pessoa))
dir(pessoa)
print(len(pessoa))

print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['cursos'])
print(pessoa['cursos'][1])
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa.get('idade'))

print('Aula 2 ---------------------------------')

pessoa = {'nome': 'Prof Alberto', 'idade': 43, 'cursos': ['React', 'Python']}
pessoa['idade'] = 44
pessoa['cursos'].append('Angular')
print(pessoa)

# Retira uma chave do dicionario
pessoa.pop('idade')
print(pessoa)
# Adiciona novas chaves ao dicionario, nova ordem
pessoa.update({'idade': 40, 'sexo': 'M'})
print(pessoa)

# Deleta Alguma chave
del pessoa['cursos']
print(pessoa)
# pessoa.clear()
print(pessoa)
