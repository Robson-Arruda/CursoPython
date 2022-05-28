from classes import *

cliente1 = Cliente('Robson', 33)
cliente1.insere_endereco('Taubaté', 'SP')
print(cliente1.nome, cliente1.idade)
cliente1.lista_enderecos()
cliente1.falar()
cliente1.comprar()
del cliente1
print()

aluno1 = Aluno('João', 45)
aluno1.insere_endereco('Belo Horizonte', 'MG')
print(aluno1.nome, aluno1.idade)
aluno1.lista_enderecos()
aluno1.falar()
aluno1.estudar()
del aluno1
print()
