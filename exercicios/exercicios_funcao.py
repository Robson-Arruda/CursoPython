"""
1 - Crie uma função que exibe uma saudação com os parâmetros
saudação e nome
"""


def saudacao(msg=input('Qual é a Saudação? '), nome=input('Qual seu nome? ')):
    return f'{msg} {nome}'


boas_vindas = saudacao()
print(boas_vindas)

"""
2 - Crie uma função que recebe 3 números como parâmetros e
exiba a soma entre eles
"""


def mensagem_soma(n1=int(input('1° núm: ')), n2=int(input('2° núm: ')), n3=int(input('3° núm: '))):
    return n1 + n2 + n3


soma = mensagem_soma()
print(f'A soma dos números é {soma}')


"""
3- Crie uma função que receba 2 números. O primeiro é um valor e o segundo
um percentual (ex.10%). Retorne o valor do número somado do aumento
so percentual do mesmo
"""


def percentual(n1=int(input('Digite um número ')), n2=int(input('Quer somar quantos porcento no número digitado? '))):
    return n1+((n1/100) * n2)


porcentagem = percentual()
print(porcentagem)


"""
4 - Fizz Buzz - Se o parametro da função for divisivel por 2, retorne fizz,
se o parametro da função for divisivel por 5, retorne Buzz.
Se o parãmetro da função for divisivel por 5 e 3, retorne FizzBuzz, caso contrario retorne
o número enviado
"""


def fizzbuzz(n=int(input('Digite um número: '))):
    if n % 5 == 0 and n % 3 == 0:
        return 'FizzBuzz'
    if n % 3 == 0:
        return 'Fizz'
    if n % 5 == 0:
        return 'Buzz'
    return n


variavel = fizzbuzz()
print(variavel)
