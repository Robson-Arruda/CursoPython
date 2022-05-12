l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ex1 = [valor for valor in l1]
print(ex1)

ex2 = [valor * 2 for valor in l1]
print(ex2)

ex3 = [(valor, valor2) for valor in l1 for valor2 in range(2)]
print(ex3)

l2 = ['Robson', 'Thelma', 'João']
ex4 = [valor.replace('o', '@').upper() for valor in l2]
print(ex4)

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2')
)
ex5 = [(y, x) for x, y in tupla]
ex5 = dict(ex5)
print(ex5['valor2'])

l3 = list(range(100))
ex6 = [valor for valor in l3 if valor % 3 == 0 if valor % 8 == 0]
print(ex6)

ex7 = [valor if valor % 3 == 0 and valor % 8 == 0 else 0 for valor in l3]
print(ex7)
