"""
count - iterttols
"""

from itertools import count

# contador = count(start=5, step=0.05)
#
# for valor in contador:
#     print(round(valor, 2))
#
#     if valor >= 10:
#         break

contador = count()
lista = ['Robson', 'Thelma', 'Maria', 'Mercia', 'João']
lista = zip(contador, lista)
print(list(lista))
