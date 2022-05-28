class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} esta falando...')

    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self):
        print(f'{self.nome} {self.idade} ANOS FOI APAGADO')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} esta comprando...')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} esta estudando...')


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.cidade}/{self.estado} FOI APAGADO')