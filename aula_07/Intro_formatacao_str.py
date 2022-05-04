nome = input('Qual seu nome? ')
ano_nascimento = input('nasceu em qual ano? ')
altura = input('Qual sua altura? ')
ano_atual = input('em qual ano estamos? ')
maior_idade = int(ano_atual) - int(ano_nascimento)
peso = input('qual seu peso? ')
idade = int(ano_atual) - int(ano_nascimento)
imc = float(peso) / (float(altura) ** 2)

# Utilizando f string
print(f'{nome} tem {idade} anos de idade e seu IMC é {imc:.2f}')

# Utilizando format
print('{} tem {} anos e seu IMC é {:.2f}'.format(nome, idade, imc))

# Utilizando format com índice
print('o nome pode aparecer novamente "{0}", o valor do IMC agora "{2:.2f}" '
      'a frase normal: {0} tem {1} anos e seu IMC é {2:.2f}'.format(nome, idade, imc))

# Utilizando format com parâmetros nomeados
print('o nome pode aparecer novamente "{n}", o valor do IMC agora "{im:.2f}" '
      'a frase normal: {n} tem {i} anos e seu IMC é {im:.2f}'.format(n=nome, i=idade, im=imc))
