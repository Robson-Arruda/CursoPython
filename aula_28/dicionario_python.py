"""
dicionário é muito parecido com listas, porém em listas o índice
é gerado automaticamente, enquanto no dicionário o índice é inserido
manualmente.
"""

# d1 = {'chave1': 'valor da chave'}
# d1['novachave'] = 'valor da nova chave'
#
# print(d1['novachave'])

# d1 = dict(chave1='Valor da chave', chave2='valor da outra chave')
# d1['chave3'] = 'valor da terceira chave'
#
# print(d1)

# d1 = {
#     'str': 'String como chave',
#     123: 'Números como chave',
#     (1, 2, 3, 4): 'Tupla como chave'
#     }
# d1['naoexiste'] = 'Agora existe'
# # print(d1)
# if 'naoexiste' in d1:
#     print(d1['naoexiste'])
# print('oi')

# d1 = {
#     'str': 'String como chave',
#     123: 'Números como chave',
#     (1, 2, 3, 4): 'Tupla como chave'
#     }
#

# d1 = {
#     'str': 'String como chave',
#     123: 'Números como chave',
#     (1, 2, 3, 4): 'Tupla como chave'
#     }
# # d1['str'] = 'agora ela existe'
# if d1.get('str') is not None:
#     print(d1.get('str'))
# print(1234)
#
# d1 = {
#     'str': 'String como chave',
#     123: 'Números como chave',
#     (1, 2, 3, 4): 'Tupla como chave'
#     }


# d1 = {
#     'str': 'String como chave',
#     123: 'Números como chave',
#     (1, 2, 3, 4): 'Tupla como chave'
#     }
# d1.update({'nova_chave': 'novo_valor'})
# if d1.get('nova_chave') is not None:
#     print(d1.get('nova_chave'))
# print(1234)

# d1 = {
#     'str': 'String como chave',
#     123: 'Números como chave',
#     (1, 2, 3, 4): 'Tupla como chave'
#     }
# d1.update({'nova_chave': 'novo_valor'})
# if d1.get('nova_chave') is not None:
#     print(d1.get('nova_chave'))
# print(d1)
# del d1['str']
# print(d1)
#
# d1 = {
#     'str': 'String como chave',
#     123: 'Números como chave',
#     (1, 2, 3, 4): 'Tupla como chave'
#     }
#
# print('str' in d1)
# print('str' in d1.keys())
# print('Números como chave' in d1.values())
# print(len(d1))
#
# for key in d1:  # Iterando sobre as chaves
#     print(key)
#
# for v in d1.values():  # Iterando sobre os valores
#     print(v)
#
# for k in d1.items():  # Iterando sobre as chaves e valores
#     print(k)
#
# for k, v in d1.items():  # Desempacotando Dicionário
#     print(k, v)

# Exibindo lista de clientes EXEMPLO:

# clientes = {
#     'cliente1': {
#         'Nome': 'Robson',
#         'Sobrenome': 'Arruda',
#     },
#     'cliente2': {
#         'Nome': 'Thelma',
#         'Sobrenome': 'Souza',
#     },
#     'cliente3': {
#         'Nome': 'João',
#         'Sobrenome': 'Souza',
#     },
# }
#
# for clientes_k, clientes_v in clientes.items():
#     print(f'Exibindo {clientes_k}')
#     for dados_k, dados_v in clientes_v.items():
#         print(f'\t{dados_k} = {dados_v}')
#
# # Criando uma cópia raza do dicionário, permite alterar valores mutáveis

# print('**********    CÓPIA RAZA    *********** ')
# d1 = {1: 'a', 2: 'a', 3: 'a', 4: 'a', 'e': ['Robson', 'Arruda']}
# print(f'{d1} Esse é o original')
# v = d1.copy()
# v[1] = 'João'
# v['e'][0] = 'Thelma'
# print(f'{d1} Esse é o original "d1" FOI alterado')
# print(v)

# Criando uma cópia real
#
# print(' ')
# print('**********    CÓPIA PROFUNDA    *********** ')
# import copy
# d1 = {1: 'a', 2: 'a', 3: 'a', 4: 'a', 'e': ['Robson', 'Arruda']}
# print(f'{d1} Esse é o original')
# v = copy.deepcopy(d1)
# v[1] = 'João'
# v['e'][0] = 'Thelma'
# print(f'{d1} Esse é o original "d1" não foi alterado')
# print(v)

# Convertendo  lista em dicionário
#
# lista = [
#     ('c1', 1),
#     ('c2', 2),
#     ('c3', 3),
# ]
# d1 = dict(lista)
# print(d1)

# Eliminando a última chave do dicionário

d1 = {
    'str': 'String como chave',
    123: 'Números como chave',
    (1, 2, 3, 4): 'Tupla como chave'
    }
d1.popitem()
print(d1)

# Eliminando qualquer chave do dicionário
#
# d1 = {
#     'str': 'String como chave',
#     123: 'Números como chave',
#     (1, 2, 3, 4): 'Tupla como chave'
#     }
# d1.pop(123)  # É preciso indicar a chave
# print(d1)

# Contatenando 2 dicionários

d1 = {
    1: 4,
    2: 5,
    3: 6,
    }
d2 = {
    4: 7,
    5: 8,
    6: 9
}
print(d1)
print(d2)
d1.update(d2)
print(d1)
