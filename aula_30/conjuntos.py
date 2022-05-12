# MUITO UTILIZADO PARA ELIMINAR ELEMENTOS DUPLICADOS EM UMA LISTA
# ATENÇÃO OS ITENS DA LISTA VOLTARÃO SEM REPETIÇÃO MAS FORA DE ORDEM!

# add (adiciona), update (atualiza), clear, discard
# union | (une)
# intersection & (Todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^(Elementos que estão nos dois sets, mas não em ambos)
# SET NÃO ACEITA ELEMENTOS DUPLICADOS

# s1 = {1, 2, 3, 4, 5, 6}
# print(s1)
#
# s1 = set()
# s1.add(1)
# s1.add(2)
# s1.add((1, 2, 3, 'Robson'))
# print(s1)
#
# s1.discard(2)
# print(s1)
#
# s1.update('a')
# print(s1)
#
# s1.update('Phython')  # Update itera a palavra letra por letra.
# print(s1)
#
# s1.discard('P')
# print(s1)

# print('Eliminando elementos duplicados')
#
# l1 = [1, 2, 3, 2, 2, 3, 3, 5, 5, 7, 'robson', 'robson']
# print('lista "l1" original')
# print(l1)
# l1 = set(l1)
# print('lista "l1" transfomada em conjunto "set"')
# print(l1)
# l1 = list(l1)
# print('lista "l1" como lista e sem elementos duplicados')
# print(l1)

# Unindo 2 sets / conjuntos

s1 = {1, 2, 3, 4, 5, 8, 7}
s2 = {1, 2, 3, 4, 5, 6, 8}
s3 = s1 | s2
print(s3)

# Intersection, valores presentes nos dois conjuntos
s1 = {1, 2, 3, 4, 5, 8, 7}
s2 = {1, 2, 3, 4, 5, 6, 8}
s3 = s1 & s2
print(s3)

# Mostra elemento que está somente no set da ESQUERDA.
s1 = {1, 2, 3, 4, 5, 8, 7}
s2 = {1, 2, 3, 4, 5, 6, 8}
s3 = s1 - s2  # Elemento que está somente no s1 '7'
print(s3)

# Elementos que estão nos dois sets mas não em ambos
s1 = {1, 2, 3, 4, 5, 8, 7}
s2 = {1, 2, 3, 4, 5, 6, 8}
s3 = s1 ^ s2
print(s3)
