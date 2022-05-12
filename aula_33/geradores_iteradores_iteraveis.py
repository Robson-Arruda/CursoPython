import sys
import time

# Iteráveis

# lista = [0, 1, 2, 3, 4, 5]
# print(hasattr(lista, '__iter__'))   # Verificando é é iterável

# lista = 123456
# print(hasattr(lista, '__iter__'))   # Verificando é é iterável
#
# lista = 'String'
# print(hasattr(lista, '__iter__'))   # Verificando se é iterável

# O laço for transforma a lista em um iterador, iterador tem a função NEXT
#
# lista = [0, 1, 2, 3, 4, 5]
# lista = iter(lista)
# print(next(lista))
# print(next(lista))
# print(next(lista))
#
# print(hasattr(lista, '__next__'))   # Verificando se é iterador

# Gerador normalmente utilizado para ações que levarão muito tempo para serem digitados ou usarão muita memória


# lista = list(range(100))
# print(lista)
# print(sys.getsizeof(lista))  # Exibe quantos bytes de memória a variável lista está consumindo
#

# def gera():
#     for n in range(100):
#         yield n
#         time.sleep(0.1)
#
#
# g = gera()
#
# for v in g:
#     print(v)
#
# def gera():
#     variavel = 'valor 1'
#     yield variavel
#     variavel = 'valor 2'
#     yield variavel
#     variavel = 'valor 3'
#     yield variavel
#
#
# g = gera()
#
# for v in g:
#     print(v)

lista = [x for x in range(10000)]
print(type(lista))
print(sys.getsizeof(lista))

lista = (x for x in range(10000))  # ESSE É UM GERADOR!! UTILIZA MUITO MENOS MEMÓRIA
print(type(lista))
print(sys.getsizeof(lista))
