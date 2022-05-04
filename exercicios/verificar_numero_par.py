"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. caso o usuário não digite um número
inteiro, informe que não é um numero inteiro
"""
num = input('Digite um número INTEIRO: ')

if num.isnumeric():
    num = int(num)
    resto = num % 2
    if resto != 0:
        print(f'{num} é ímpar')
    else:
        print(f'{num} é par')

else:
    print('Você não digitou um número inteiro. ')
