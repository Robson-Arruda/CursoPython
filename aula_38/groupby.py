"""
Agrupando elementos em dicinários
"""
from itertools import groupby, tee

alunos = [
    {'nome': 'Robson', 'nota': 'A'},
    {'nome': 'Thelma', 'nota': 'A'},
    {'nome': 'João', 'nota': 'B'},
    {'nome': 'Valéria', 'nota': 'C'},
    {'nome': 'Ana', 'nota': 'B'},
    {'nome': 'Jandira', 'nota': 'D'},
    {'nome': 'Sérgio', 'nota': 'C'},
    {'nome': 'Cesar', 'nota': 'D'},
    {'nome': 'Gustavo', 'nota': 'A'},
    {'nome': 'Lenadro', 'nota': 'E'},
]

ordena = (lambda item: item['nota'])
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)
    print(f'Alunos com nota {agrupamento}:')

    for aluno in va1:
        print(f'\t{aluno}')
    quantidade = len(list(va2))
    print(f'\t{quantidade} alunos tiraram a nota {agrupamento}\n')
