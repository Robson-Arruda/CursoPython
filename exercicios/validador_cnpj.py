import re

cnpj = input('Digite um CNPJ:\n')


def apenas_numeros(cnpj_format):
    return re.sub(r'\D', '', cnpj_format)


def validador_cnpj():
    cnpj1 = apenas_numeros(cnpj)
    multiplicador_d1 = 5
    multiplicador_d2 = 6
    soma = 0
    temp_cnpj = ''
    compara_cnpj = ''
    limite = 0

    for num in cnpj1:
        if num != '.' and num != '/' and num != '-' and num != ' ':
            compara_cnpj = compara_cnpj + num

            if limite < 12:
                soma = soma + (int(num) * multiplicador_d1)
                temp_cnpj = temp_cnpj + num
                multiplicador_d1 -= 1
                limite += 1
                if multiplicador_d1 < 2:
                    multiplicador_d1 = 9

    dg1 = 11 - (soma % 11)
    if dg1 > 9:
        dg1 = 0
    novo_cnpj = temp_cnpj + str(dg1)

    soma = 0
    limite = 0
    temp_cnpj = ''

    for numero in novo_cnpj:
        if numero != '.' and numero != '/' and numero != '-':
            if limite < 13:
                temp_cnpj = temp_cnpj + numero
                soma = soma + (int(numero) * multiplicador_d2)
                multiplicador_d2 -= 1
                limite += 1

                if multiplicador_d2 < 2:
                    multiplicador_d2 = 9
            else:
                break
    dg2 = 11 - (soma % 11)
    if dg2 > 9:
        dg2 = 0
    temp_cnpj = temp_cnpj + str(dg2)
    return temp_cnpj == compara_cnpj


if validador_cnpj():
    print('CNPJ Válido')
else:
    print('CNPJ Inválido')
