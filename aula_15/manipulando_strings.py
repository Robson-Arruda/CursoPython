"""
Manipulando Strings
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funões Built-in len, abs, type, print, etc...
Essa funções podem serem usadas diretamente em cada tipo.
"""
#  cada letra do texto tem um índice
texto = 'Python_s2'
# Acessando índices positivos
print(texto[2])  # Acessando o 't' da palavra Python
print(texto[5])  # Acessando o 'n' da palavra Python

# Acessando índices negativos
print(texto[-1])  # Acessando o último indice da variável
print(texto[-6])  # Acessando o 6° indice de trás pra frente da var

# Fatiamento
nova_string = texto[1:-1]
# Primeiro valor do [] indice da primeira letra e segundo valor indice da última letra
print(nova_string)
url = 'www.google.com.br/'
print(url[:-1])  # Excluindo o ultimo caracter '/'
print(texto[0:-1:2])  # Adicionando STEP ou seja passos, nesse caso de 2 em 2
