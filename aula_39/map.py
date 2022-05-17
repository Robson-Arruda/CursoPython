from dados import produtos, pessoas, lista


# nova_lista = map(lambda x: x * 2, lista)
# print(list(nova_lista))
# novalista = [x * 2 for x in lista]
# print(novalista)

# Gerando uma lista somente com os preços dos produtos
# precos = map(lambda p: p['preco'], produtos)
#
# for preco in precos:  # Acrescentando 15% no valor do preço
#     atualizado = ((preco * 15) / 100) + preco
#     print(f'{atualizado:.2f}')

# aumentando preço com função

def aumenta_preço(p):
    p['preco'] = round(p['preco'] * 1.15, 2)
    return p


precos_atualizados = map(aumenta_preço, produtos)

for produto in precos_atualizados:
    print(produto)
print('\n\n')

nomes = map(lambda p: p['nome'], pessoas)

for pessoa in nomes:
    print(pessoa)
