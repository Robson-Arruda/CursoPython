from classes import Cliente

cliente1 = Cliente('Robson', 33)
cliente1.insere_endereco('Taubaté', 'SP')
print(cliente1.nome, cliente1.idade)
cliente1.lista_enderecos()
del cliente1
print()

cliente2 = Cliente('Thelma', 39)
cliente2.insere_endereco('Caraguatatuba', 'SP')
print(cliente2.nome, cliente2.idade)
cliente2.lista_enderecos()
del cliente2
print()

cliente3 = Cliente('João', 69)
cliente3.insere_endereco('Salvador', 'BA')
cliente3.insere_endereco('São Paulo', 'SP')
print(cliente3.nome, cliente3.idade)
cliente3.lista_enderecos()
del cliente3
print()

cliente4 = Cliente('Jayr', 25)
cliente4.insere_endereco('Governador Valadares', 'MG')
print(cliente4.nome, cliente4.idade)
cliente4.lista_enderecos()

print()
print('#####################################################################')