from dados import produtos, pessoas, lista
from functools import reduce

# Reduce é uma forma mais ágil de criar um acumulador
soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(f'Soma de todos os valores da lista {soma_lista}\n')

soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(f'Valor total da soma de todos os produtos R${round(soma_precos, 2)}')
print(f'O valor médio dos produtos é R${round(soma_precos / len(produtos), 2)}\n')

soma_idade = reduce(lambda ac, p: p['idade'] + ac, pessoas, 0)
print(f'A idade de todas as pessoas somandas é de {soma_idade}\n')
print(f'A média de idade das pessoas é de {round(soma_idade / len(pessoas))} anos')
