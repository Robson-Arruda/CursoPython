"""
Operador ternário em Python
"""
logged_user = False
msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar'

print(msg)

idade = input('Qual sua idade? ')

if not idade.isnumeric():
    print('Digite apenas números')
else:
    idade = int(idade)
    e_maior = (idade >= 18)
    msg1 = 'Pode acessar' if e_maior else 'Não pode acessar'
    print(msg1)
