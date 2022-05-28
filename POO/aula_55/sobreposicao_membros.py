from classes import *

cliente1 = Cliente('Robson', 33)
print(cliente1.nome, cliente1.idade)
cliente1.comprar()
print()

cliente1vp = ClienteVip('Thelma', 39)
print(cliente1vp.nome)
cliente1vp.falar()
print()

cliente1svp = ClienteSuperVip('João', 'Souza', 50)
print(cliente1svp.nome, cliente1svp.sobrenome, cliente1svp.idade)
cliente1svp.falar()