"""if __name__ == '__main__' é utilizado para que os testes realizados no arquivo de origem não sejam
execultados no arquivo principal, pois o arquivo quando executado na origem tem o nome '__main__', já quando
executado no arquivo principal, passa a ter o nome do arquivo mesmo. Dessa forma o teste é execultado após
o 'if__name__ == '__name__' ' """

from modulo import soma

print(soma(50, 80))

