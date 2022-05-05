"""
Laços de repetição while e for
como ja possuo conhecimento prévio sobre,
essa aula foi pulada
"""
sair = 'n'

while sair == 'n':
    contador = 0
    erro = 0
    print()
    num_1 = input('digite um número: ')
    operador = input('Digite um operador: ')
    num_2 = input('digite outro número: ')
    '''if not num_1.isnumeric() or not num_2.isnumeric():
        print('você precisa digitar um número.')
        continue'''

    try:
        num_1 = float(num_1)
        num_2 = float(num_2)

        #  + - / *
        if operador == '+':
            print(num_1 + num_2)
            sair = input('Deseja sair? [s]im ou [n]ão: ')
            sair = sair.lower()
        elif operador == '-':
            print(num_1 - num_2)
            sair = input('Deseja sair? [s]im ou [n]ão: ')
            sair = sair.lower()
        elif operador == '*':
            print(num_1 * num_2)
            sair = input('Deseja sair? [s]im ou [n]ão: ')
            sair = sair.lower()
        elif operador == '/':
            print(num_1 / num_2)
            sair = input('Deseja sair? [s]im ou [n]ão: ')
            sair = sair.lower()
        else:
            print('Digite um operador válido')
            print('Reiniciando a calculadora')
        if sair != 'n' and sair != 's':
            erro = 1
            while erro == 1:
                sair = input('Valor digitado incorreto. Deseja sair? [s]im ou [n]ão: ')
                sair = sair.lower()
                contador = contador + 1
                if contador == 3:
                    print('Número de tentativas excedidas')
                    print('Finalizando o programa')
                    break
                if sair == 'n' or sair == 's':
                    erro = 0
    except:
        print('Digite somente números.')
        print('Reiniciando a calculadora')
