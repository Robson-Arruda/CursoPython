from random import randint
primeiro = str(randint(0, 9))
segundo = str(randint(0, 9))
terceiro = str(randint(0, 9))
temp_cnpj = primeiro + segundo + terceiro + str(randint(10000, 99999))
mil_contra = '0001'
cnpj = temp_cnpj + mil_contra


def gerador_cnpj():
    multiplicador_d1 = 5
    multiplicador_d2 = 6
    soma = 0
    limite = 0

    for num in cnpj:
        if limite < 12:
            soma = soma + (int(num) * multiplicador_d1)
            multiplicador_d1 -= 1
            limite += 1

        if multiplicador_d1 < 2:
            multiplicador_d1 = 9

    dg1 = 11 - (soma % 11)

    if dg1 > 9:
        dg1 = 0
    novo_cnpj = cnpj + str(dg1)

    soma = 0

    for numero in novo_cnpj:
        soma = soma + (int(numero) * multiplicador_d2)
        multiplicador_d2 -= 1
        if multiplicador_d2 < 2:
            multiplicador_d2 = 9

    dg2 = 11 - (soma % 11)

    if dg2 > 9:
        dg2 = 0
    novo_cnpj = novo_cnpj + str(dg2)
    return novo_cnpj


final = gerador_cnpj()
print(f'{final[:2]}.{final[2:5]}.{final[5:8]}/{final[8:12]}-{final[12:14]}')
