"""
import csv

with open('desafio_ibge.csv', 'r', encoding='ISO-8859-1') as arquivo:
    leitor = csv.reader(arquivo)
    header = next(leitor)
    for linha in in leitor
        print('Nome: {}, Idade: {}'.format())
"""
import csv
from urllib import request


def read(url):
    with request.urlopen(url) as entrada:
        print('Baixando o CSV...')
        dados = entrada.read().decode('latin1')
        print('Dowbload completo!')
        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]}: {cidade[3]}')


if __name__ == '__main__':
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
