from dados import produtos, pessoas, lista


# Filtrando na lista valores maior que 5

# nova_lista = filter(lambda x: x > 5, lista)
# print(list(nova_lista))

# Filtrando produtos com valor acima de 10.00

# novo_produto = filter(lambda p: p['preco'] > 30, produtos)
# print('Mostrando produtos maiores que 30 reais:\n')
# for produto in novo_produto:
#     print(produto)

# Utilizando Função:


def filtra(produtos):
    if produtos['preco'] > 20:
        return True


novo_produto = filter(filtra, produtos)

for produto in novo_produto:
    print(produto)

print('\n\n')
print('Exibindo pessoas com idade maior que 18 anos\n')


def filtra(pessoa):
    if pessoa['idade'] >= 18:
        return True


maior_de_idade = filter(filtra, pessoas)

for idade in maior_de_idade:
    print(f"{idade['nome']} tem {idade['idade']} de idade")
