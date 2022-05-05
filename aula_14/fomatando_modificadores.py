"""
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(número)f - quantidade de casas decimais (float)
:(caractere)(> ou < ou ^)(quantidade)(Tipo - s,d ou f)

> - Esquerda
< - Direita
^ - Centro
"""
num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print('{:.2f}'.format(divisao))  # Utilizando .format()
print(f'{divisao:.2f}')  # Utilizando Fstring

# Formatando String
nome = 'Robson arruda'
print(f'{nome:s}')
print(f'{nome:*^25}')
nome_formatado = '{:@>25}'.format(nome)
print(nome_formatado)
print(nome.lower())  # Tudo minúsculo
print(nome.upper())  # Tudo Maiúsculo
print(nome.title())  # Primeiras letras Maiúsculas

# Adicionando quantidade de digitos em um numero
print(f'{num_2:0>10}')  # Nesse exemplo adicionei '0' a esquerda da var até atingir 10 digitos
print(f'{num_2:2>10}')  # Nesse exemplo adicionei '2' a esquerda da var até atingir 10 digitos
print(f'{num_2:0<10}')  # Nesse exemplo adicionei '0' a direita da var até atingir 10 digitos
print(f'{num_2:0^10}')  # Nesse exemplo adicionei '0' no centro da var até atingir 10 digitos
print(f'{num_2:.2f}')  # Nesse exemplo transformei a var em float e adicionei 2 casas decimais
print(f'{num_2:0>10.2f}')  # Nesse exemplo transformei a var em float e adicionei '0'a esquerda totalizando 10 casas]

