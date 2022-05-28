class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} esta falando...')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} esta comprando...')

    def falar(self):
        print('Estou em Cliente')


class ClienteVip(Cliente):
    def falar(self):
        Pessoa.falar(self)
        super().falar()
        print('Outra coisa qualquer.')


class ClienteSuperVip(Cliente):
    def __init__(self, nome, sobrenome, idade):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome} está falando....')
