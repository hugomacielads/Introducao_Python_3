from decimal import Decimal, getcontext

print(dir(int))
print(dir(float))

a = 5
b = 2.5
a / b
a + b
a * b

print(a / b)

print(b.is_integer())
print(5.0.is_integer())

print(int.__add__(2, 3))

print((-2).__abs__())
abs(-2)

print((-3.6).__abs__())
print(abs(-3.6))

# Manipulação de números

# print(1.1 + 2.2)

Decimal(1) / Decimal(7)

# Quantidade de casas
getcontext().prec = 4
Decimal(1) / Decimal(7)
Decimal.max(Decimal(1), Decimal(7))
dir(Decimal)

print(1.1 + 2.2)
print(Decimal(1.1) + Decimal(2.2))

# Podemos trabalhar com arredondamentos com .format
# Utilizamos o Decimal quando a precisão é de extrema importância
