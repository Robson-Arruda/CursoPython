"""
Iniciar com letra, pode conter números, separa com _, letras minúsculas
"""
nome = input('Qual seu nome? ')
ano_nascimento = input('nasceu em qual ano? ')
ano_nascimento = int(ano_nascimento)
altura = input('Qual sua altura? ')
altura = float(altura)
print(nome, type(nome))
ano_atual = input('em qual ano estamos? ')
ano_atual = int(ano_atual)
maior_idade = ano_atual - ano_nascimento
peso = input('qual seu peso? ')
peso = float(peso)

if maior_idade >= 18:
    print(nome, 'é maior de idade')
else:
    print(nome, 'é menor de idade')
