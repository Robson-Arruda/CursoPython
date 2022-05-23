# https://docs.python.org/3/library/functions.html#open
import os  # Utilizado para apagar arquivos
import json

try:
    file = open('abc.txt', 'w+')
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

    file.seek(0, 0)
    print('Lendo Linhas:')
    print(file.read())
    print('###########')

    file.seek(0, 0)
    print(file.readline(), end='')
    print(file.readline(), end='')
    print(file.readline(), end='')

    print('###########')

    file.seek(0, 0)
    print(file.readlines())

    print('###########')
    file.seek(0, 0)
    for linha in file.readlines():
        print(linha, end='')

    print('###########')
    file.seek(0, 0)
    for linha in file:
        print(linha, end='')
finally:
    file.close()

print('###########')
# UTILIZANDO GERENCIADORES DE CONTEXTO

with open('abc.txt', 'w+') as file:  # Vai sobrescrever os dados do arquivo
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

    file.seek(0)
    print(file.read())

print('###########')

with open('abc.txt', 'a+') as file:  # Vai adicionar os dados no arquivo
    file.write('Linha 4\n')
    file.write('Linha 5\n')
    file.write('Linha 6\n')

    file.seek(0)
    print(file.read())

print('###########')

with open('abc.txt', 'r') as file:  # Vai ler o arquivo

    file.seek(0)
    print(file.read())
# O GERENCIADOR DE CONTEXTO FECHA O ARQUIVO AUTOMÁTICAMENTE

# APAGANDO ARQUIVO

# os.remove('abc.txt') # Deixarei comentado para não apagar o arquivo gerado

d1 = {
    'Pessoa 1': {
        'nome': 'Robson',
        'idade': 33,
    },
    'Pessoa 2': {
        'nome': 'Thelma',
        'idade': 39,
    },
}

d1_json = json.dumps(d1)
with open('pessoas.json', 'w+') as file:
    file.write(d1_json)
    
