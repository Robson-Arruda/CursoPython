from log import LogMixin


class Eletronico(LogMixin):
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            error = f'{self._nome} Já está ligado.'
            print(error)
            self.log_error(error)
            return
        info = f'Ligando {self._nome}...'
        print(info)
        self.log_info(info)
        self._ligado = True

    def desligar(self):
        if not self._ligado:
            error = f'{self._nome} já desligado...'
            print(error)
            self.log_error(error)
            return
        info = f'Desligando {self._nome}...'
        print(info)
        self.log_info(info)
        self._ligado = False


class Smartphone(Eletronico):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            error = f'{self._nome} Não está ligado, impossível conctar!'
            print(error)
            self.log_error(error)
            return
        if self._conectado:
            error = f'{self._nome} Já está conectado!'
            print(error)
            self.log_error(error)
            return
        info = f'Conectando {self._nome}'
        print(info)
        self.log_info(info)
        self._conectado = True

    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} Já está desconectado, impossível desconctar!'
            print(error)
            self.log_error(error)
            return
        info = f'{self._nome} Desconectando...'
        print(info)
        self.log_info(info)
        self._conectado= False
