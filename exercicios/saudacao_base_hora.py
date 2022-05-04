"""
Faça um programa que pergunte a hora ao usuário e, baseanso-se no horário
descrito, exiba a saudação apropriada. EX:
Bom dia 0-11, Boa tarde 12-17 e boa noite 18-23.
"""

hora = input('Que horas são? (0-23) ')
if hora.isnumeric():
    hora = int(hora)
    if 0 <= hora <= 11:
        print('Bom dia!')
    elif 12 <= hora <= 17:
        print('Boa tarde!')
    elif 18 <= hora <= 23:
        print('boa noite!')
    else:
        print('Valor invalido entre com valor entre 0 e 23')
else:
    print('Valor digitado não pode ser lido, entre com valor inteiro de 0 a 23, não adicione minutos.')
