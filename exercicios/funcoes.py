"""
1 - Crie uma função1 que recebe uma função2 como parametro e
retorne o valor da função2 executada
"""


# def func1():
#    return 'Olá'
#
#
# def mestre(func):
#     return func()
#
#
# executando = mestre(func1)
# print(executando)

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


executando = mestre(fala_oi, 'Robson')
executando2 = mestre(saudacao, 'Robson', saudacao='Bom dia!')
print(executando)
print(executando2)





"""
2 - Crie uma função1 que recebe uma função2 com parâmetro
e retone o valor da função 2 executada. faça a função1 executar
duas funçoes que recebam um numero diferente de argumentos
"""