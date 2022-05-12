carrinho = []

carrinho.append(('Produto 1', 25.33))
carrinho.append(('Produto 2', 40.58))
carrinho.append(('Produto 1', 37.47))
carrinho.append(('Produto 1', 42.96))
carrinho.append(('Produto 1', 15.00))
carrinho.append(('Produto 1', 17.69))
carrinho.append(('Produto 1', 48.87))
carrinho.append(('Produto 1', 12.11))

total = sum([produto[1] for produto in carrinho])
print(f' Valor do carrinho é {total}')
