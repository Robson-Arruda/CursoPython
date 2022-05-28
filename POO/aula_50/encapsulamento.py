"""
Em outras linguagens, utilizamos modificadores de acesso, onde temos métodos e atributos públicos, o acesso é
consentido ou não através do uso de: public (público), protected (protegido), private (privado).

Em python é utilizado por convenção 1 underline antes do atributo para "Não Recomendado acessar fora da classe" porém
o atributo fica acessivel fora da classe ou 2 underlines para "FORTEMENTE NÃO RECOMENDADO ACESSAR FORA DA CLASSE" e
dessa forma o atributo dica inacessível fora da classe.

Ditado: "Programador de Python é adulto e vacinado, portanto deveria respeitar a convenção".

ATENÇÃO: O MESMO É VALIDO PARA OS MÉTODOS.
"""


class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]
        pass


bd = BaseDeDados()
bd.inserir_cliente(1, 'Robson')
bd.inserir_cliente(2, 'Thelma')
bd.inserir_cliente(3, 'João')
bd.inserir_cliente(4, 'Jayr')
bd.lista_clientes()

print('**********//************')

bd.apaga_cliente(3)
bd.lista_clientes()
