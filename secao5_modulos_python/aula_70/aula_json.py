"""
JavaScript object Notation - JSON
JSON é um formato de troca de dados entre sistemas e programas muito leve
e de fácil utilização. Muito utilizado em APIs
"""

from dados import *
import json
dados_json = json.dumps(clientes_dicionario, indent=4)
print(dados_json)

dicionario = json.loads(clientes_json)

print("###################################\n")

for chave, valor in dicionario.items():
    print(chave)
    print(valor)

with open('clientes.json', 'w') as arquivo:
    json.dump(clientes_dicionario, arquivo, indent=4)

with open('clientes.json', 'r') as arquivo:
    dados = json.load(arquivo)

print(dados)