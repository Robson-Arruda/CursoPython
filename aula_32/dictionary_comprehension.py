lista = [('chave', 'valor'),
         ('chave1', 'valor1'),
         ]

# d1 = {x.upper(): y.upper() for x, y in lista}
# print(d1)

d1 = {f'chave_{x}': x**2 for x in range(5)}
print(d1)

