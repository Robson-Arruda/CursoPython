"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos

Produto - Ordem importa e repeta valores únicos
"""
from itertools import combinations, permutations, product

pessoa = ['Robson', ' Thelma', 'João', 'Maria', 'Jandira', 'Ana']

print('')
print(f'{" combinations ":*^40}')
for grupo in combinations(pessoa, 4):  # Imprime em uma ordem somente e não repete valores iguais
    print(grupo)

print('')
print(f'{" permutation ":*^40}')
for grupo in permutations(pessoa, 2):  # Imprime ordens diferentes
    print(grupo)

print('')
print(f'{" product ":*^40}')
for grupo in product(pessoa, repeat=2):  # Imprime ordem diferentes e repetes valores iguais
    print(grupo)
