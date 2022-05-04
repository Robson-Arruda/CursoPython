usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))

# Retorno do len() é sempre um inteiro

if len(usuario) < 8:  # Verificando quantidade de caracteres do usuário
    print('Insira um usuário com no mínimo 8 letras')

else:
    print('Usuário cadastrado com sucesso!')