"""
Considerando duas listas de inteiros ou floats (lista_a e lista_b),
Some o valor das listas, retornando uma nova lista com os valores somados

Se uma lista for menor que a outra, a soma só irá considerar o tamanho da menor.

Exemplo:
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
lista_soma = [2, 4, 6, 8]
"""

# Minha Solução abaixo:

# def soma_lista():
#     lista_a = [1, 2, 3, 4, 5, 6, 7]
#     lista_b = [1, 2, 3, 4]
#     lista_somada= []
#     valores_lista = zip(
#         lista_a,
#         lista_b
#     )
#     for lista_a, lista_b in valores_lista:
#         lista_somada.append(lista_a + lista_b)
#     return lista_somada
#
#
# lista_soma = soma_lista()
# print(lista_soma)

# Soluções paresentadas  ---> genérica:

# lista_a = [1, 2, 3, 4, 5, 6, 7]
# lista_b = [1, 2, 3, 4]
# lista_soma = []
#
# for i in range(len(lista_b)):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)

# lista_a = [1, 2, 3, 4, 5, 6, 7]
# lista_b = [1, 2, 3, 4]
# lista_soma = []
#
# for i, _ in enumerate(lista_b):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)

# Melhor Solução !!!!!
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)
