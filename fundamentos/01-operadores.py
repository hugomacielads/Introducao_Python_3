"""
    Curso de Python 3 - Cod3r 2021 (Hugo Maciel)
"""

# Operadores Aritméticos
print(2 + 3)
print(4 - 7)
print(2 * 5.3)
print(9.3 / 3)
print(9.3 // 3)  # Divisão inteira
print(2 ** 8)
print(10 % 3)

a = 12
b = a
print(a + b)

# DESAFIO
salario = 3450.45
despesas = 2456.2

percentual_comprometimento = (despesas / salario) * 100
print(percentual_comprometimento)

# Operadores Relacionais

print(3 > 4)
print(4 >= 3)
print(1 < 2)
print(3 <= 1)
print(3 != 3)
print(3 == 3)
print(1 == '2')

# Operadores de Atribuição

a = 3
a = a + 7
a += 5
print(a)

a -= 3
print(a)

a *= 2
print(a)

a /= 4
print(a)

a %= 4
print(a)

a **= 8
print(a)

a //= 256
print(a)

# Operadores Unários 1 operando

a = 3
++a

a -= 1
print(a)

# Operadores Ternários 3 operandos (if)

esta_chovendo = False
print('Hoje estou com as roupas ' + ('secas' if esta_chovendo else 'molhadas'))
print('Hoje estou com as roupas ' + ('secas', 'molhadas')[esta_chovendo])


# Operadores de Membro

lista = [1, 2, 3, 'Ana', 'Carla']
2 in lista
print('Ana' not in lista)

# Operador de Identidade
x = 3
y = x
z = 3
x is y
y is x
print(x is not z)

lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]

print(lista_a is lista_b)
print(lista_a is lista_c)
print(lista_b is not lista_c)