"""
Desempacotamento de listas
"""

string = 'Robson, João, Thelma'
lista = string.split(',')  # Criando lista a partir de uma string
lista_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_2 = ['Maria', 'José', 'Valéria', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista_2)
print(lista)
n1, n2, n3 = lista
print(n2)
n4, n5, n6, *outra_lista, ultimo_lista = lista_2
print(n4, n5, n6, outra_lista, ultimo_lista)
