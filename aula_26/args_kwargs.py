def func(a1, a2, a3, a4, a5):
    print(a1, a2, a3, a4, a5)


# func(1, 2, 3, 4, 5)
#

# def func_args(*args):  # Utilizado quando não sabemos a quantidade de argumentos
#     print(args)
#
#
# var = func_args()


# lista = [1, 2, 3, 4, 5]
# n1, n2, *n = lista
# print(n1, n2, n)

# lista = [1, 2, 3, 4, 5]
# print(*lista, sep='_')  # Utilizando '*' para desenpacotar uma lista, print aceita sep=''
#

# def func_args(*args):  # Utilizado quando não sabemos a quantidade de argumentos
#     print(args)
#     print(args[0])
#     print(args[-1])
#     print(len(args))
#
#
# func_args(1, 2, 3, 4, 5, 10, 25, 36)

def func_args(*args, **kwargs):  # Utilizado quando não sabemos a quantidade de argumentos
    print(args)
    nome = kwargs.get('nome')
    idade = kwargs.get('idade')
    if idade is not None:
        print(idade)
    else:
        print('Não digitou a idade')
    print(nome)

lista = [1, 2, 3, 4, 5, 10, 25, 36]
lista2 = [10, 20, 30, 40, 50, 60]

func_args(*lista, *lista2, nome='Robson', sobrenome='Arruda', idade=33)
