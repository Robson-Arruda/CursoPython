nome = input('Qual seu nome? ')
ano_nascimento = input('nasceu em qual ano? ')
ano_nascimento = int(ano_nascimento)
altura = input('Qual sua altura? ')
altura = float(altura)
ano_atual = input('em qual ano estamos? ')
ano_atual = int(ano_atual)
maior_idade = ano_atual - ano_nascimento
peso = input('qual seu peso? ')
peso = float(peso)
idade = ano_atual - ano_nascimento
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu IMC é', imc)

if imc < 18.5:
    print(nome, 'você está muito magro, procure um médico')
elif 18.5 <= imc <= 24.9:
    print(nome, 'Parabéns, você está no peso correto')
elif 25 <= imc <= 29.9:
    print(nome, 'você está com sobrepeso, uma dieta é recomendada')
elif 30 <= imc <= 39.9:
    print(nome, 'procure um nutricionista pois você está obeso')
elif imc > 40:
    print(nome, 'seu caso é GRAVE, procure um médico com urgência')
