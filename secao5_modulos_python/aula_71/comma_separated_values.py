"""
Comma Separated Values-CSV (Valores Separados por Vírgula)
É um formato de dados muito usado em tabelas (EXCEL, GOOGLE SHEETS), bases de dados, clientes de e-mail, etc...
"""
import csv

with open('clientes.csv', 'r') as arquivo:
    dados = csv.reader(arquivo)
    # next(dados)  # Para pular a primeira linha

    for dado in dados:
        print(dado)

print('\n########  Importando como DICIONÁRIO!!!  ###########\n')
with open('clientes.csv', 'r') as arquivo:
    dados = csv.DictReader(arquivo)

    for dado in dados:
        print(dado['Nome'], dado['Sobrenome'], dado['E-mail'], dado['Telefone'])

print('\n #####  Copiando os dados do arquivo clientes .csv para outro arquivo  #####\n')

with open('clientes.csv', 'r') as arquivo:
    dados = [x for x in csv.DictReader(arquivo)]  # Convertendo em lista

with open('cliente2.csv', 'w') as arquivo:
    escreve = csv.writer(
        arquivo,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )

    chaves = dados[0].keys()  # Inserindo a primeira linha com títulos no novo arquivo
    chaves = list(chaves)
    escreve.writerow(
        [
            chaves[0],
            chaves[1],
            chaves[2],
            chaves[3],
        ]
    )

    for dado in dados:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone'],
            ]
        )
