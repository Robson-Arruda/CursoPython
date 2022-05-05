"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
rango
"""
# texto = 'valor'
# lista = [1, 2, 3, 4, 'Robson Arruda', True, 10.5]

#        0    1    2    3     4      5        6
# lista = ['A', 'B', 'C', 'D', 'E', 'Robson', -110]
# #       -7    -6   -5   -4   -3     -2       -1
# lista[5] = 'Arruda'
# print(lista[5])
# print(lista[0:3])  # Printando 3 primeiros indices da lista na tela
# print(lista[::2])  # Printando do começo ao fim da lista step 2
# print(lista[::-1])  # Printando a lista de trás pra frente

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [l1 + l2]  # l3 é formada pela união de l1 e l2
print(l3)

l1.extend(l2)  # l1 se extendeu com os valores de l2
print(l1)
l1.extend('a')  # l1 se extendeu com o valor 'a' no final
print(l1)

l2.append('b')  # append é a função correta para inserir ítem ao fim da lita
print(l2)

l2.insert(0, 'Robson')  # função insert() insere em qq lugar da lista, basta indicar o índice de inserção
print(l2)

l2.pop()  # Função pop APAGA o ÚLTIMO índice da lista
print(l2)

print(l1)
del(l1[2:6])  # Função del() utilizada para apagar um índice ou um range de índices da lista
print(l1)

l3 = [1, 5, 9, 0, 6, 2]
print(max(l3))  # Mostra o maior valor da lista, funciona somente com lista composta por inteiros
print(min(l3))  # Mostra o MENOR valor da lista, funciona somente com lista composta por inteiros

l4 = list(range(0, 100, 8))  # Criando lista de 0 a 100 multiplos de 8
print(l4)

for valor in l4:
    print(valor)
