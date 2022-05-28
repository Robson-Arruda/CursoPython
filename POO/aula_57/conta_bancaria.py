from classes_abstratas import *


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor do deposito precisa ser Numérico')
        if self.saldo < valor:
            print(f'Sacando {valor}')
            print('#################################')
            print('Saldo Insuficiente')
            print('#################################')
            self.detalhes()
            return
        print(f'Sacando {valor}')
        print('#################################')
        self._saldo -= valor
        self.detalhes()


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=500):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor do deposito precisa ser Numérico')
        if (self.saldo + self.limite) < valor:
            print(f'Sacando {valor}')
            print('#################################')
            print('Saldo Insuficiente')
            print('#################################')
            self.detalhes()
            return
        print(f'Sacando {valor}')
        print('#################################')
        self._saldo -= valor
        self.detalhes()