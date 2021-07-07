"""
def calcula_nota(nota):
    if (nota > 10 or nota < 0):
        print('Nota inválida')
    else:
        if nota >= 9.1:
            nota_final = "A"
            print(f'Sua nota é {nota_final}')
        elif nota >= 8.1:
            nota_final = "A-"
            print(f'Sua nota é {nota_final}')
        elif nota >= 7.1:
            nota_final = 'B'
            print(f'Sua nota é {nota_final}')
        elif nota >= 6.1:
            nota_final = 'B-'
            print(f'Sua nota é {nota_final}')
        elif nota >= 5.1:
            nota_final = 'C'
            print(f'Sua nota é {nota_final}')
        elif nota >= 4.1:
            nota_final = 'C-'
            print(f'Sua nota é {nota_final}')
        elif nota >= 3.1:
            nota_final = 'D'
            print(f'Sua nota é {nota_final}')
        elif nota >= 2.1:
            nota_final = 'D-'
            print(f'Sua nota é {nota_final}')
        else:
            nota_final = 'E'
            print(f'Sua nota é {nota_final}')


print(calcula_nota(10))
"""

"""
    RESOLUÇÃO EXERCÍCIO IF, ELSE, ELIF

"""


def nota_conceito(valor):
    nota = float(valor)

    if nota > 10:
        return 'Nota inválida'
    elif nota >= 9.1:
        return 'A'
    elif nota >= 8.1:
        return 'A-'
    elif nota >= 7.1:
        return 'B'
    elif nota >= 6.1:
        return 'B-'
    elif nota >= 5.1:
        return 'C'
    elif nota >= 4.1:
        return 'C-'
    elif nota >= 3.1:
        return 'D'
    elif nota >= 2.1:
        return 'D-'
    elif nota >= 1.1:
        return 'E'
    elif nota >= 0:
        return 'E'
    else:
        return 'Nota inválida'


if __name__ == '__main__':
    valor_informado = input('Nota do aluno: ')
    conceito = nota_conceito(valor_informado)
    print(conceito)
