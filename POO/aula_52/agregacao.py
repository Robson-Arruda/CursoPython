from classes import CarrinhoDeCompras, Produtos

carrinho = CarrinhoDeCompras()
p1 = Produtos('Camiseta', 90.53)
p2 = Produtos('Jaqueta', 1749.99)
p3 = Produtos('Suporte de Celular Automotivo', 184.32)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p3)
carrinho.listar_produtos()
print(carrinho.soma_total())
