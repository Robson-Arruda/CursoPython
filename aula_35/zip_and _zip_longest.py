"""
Zip - unindo iteráveis ---- Une somente até a menor lista
Zip_longest - itertools ---- Une até a maior lista, mas iténs sem referência é preenchido com NONE
"""
from itertools import count  # Necessário para o uso do Zip_longest e do count()

indice = count()
cidades = ['Taubaté', 'Belo Horizonte', 'Londrina', 'Goiânia', 'Maceió']
estados = ['SP', 'MG', 'PR', 'GO']

cidades_estados = zip(
    indice,
    cidades,
    estados,

)

for indice, estado, cidades in cidades_estados:
    print(indice, estado, cidades)

# for valor in cidades_estados:
#     combinado = valor[0] + '-' + valor[1]  # Minha Solução
#     print(combinado)
