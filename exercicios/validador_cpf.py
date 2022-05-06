cpf = input('Insira seu CPF: ')
cpf_m1 = 10
cpf_m2 = 11
soma_multiplo = 0
soma_multiplo2 = 0
novo_cpf = ''

# Calculo para o 1° digito
if cpf.isnumeric():
    for n in cpf:
        novo_cpf = novo_cpf + n
        cpf_temp = int(n)
        multiplo_cpf = cpf_temp * cpf_m1
        cpf_m1 -= 1
        soma_multiplo = multiplo_cpf + soma_multiplo
        if cpf_m1 < 2:
            break
    # Gerando 1° Digito
    primeiro_digito = 11 - (soma_multiplo % 11)
    if primeiro_digito > 9:
        primeiro_digito = 0
        novo_cpf = novo_cpf + str(primeiro_digito)
    else:
        novo_cpf = novo_cpf + str(primeiro_digito)

    # Calculo para o 2° digito
    for n in cpf:
        cpf_temp2 = int(n)
        multiplo_cpf2 = cpf_temp2 * cpf_m2
        cpf_m2 -= 1
        soma_multiplo2 = multiplo_cpf2 + soma_multiplo2
        if cpf_m2 < 2:
            break
    # Gerando 2° Digito
    segundo_digito = 11 - (soma_multiplo2 % 11)
    if segundo_digito > 9:
        segundo_digito = 0
        novo_cpf = novo_cpf + str(primeiro_digito)
    else:
     novo_cpf = novo_cpf + str(segundo_digito)

    # Validando CPF
    sequencia = novo_cpf == str(novo_cpf[0] * 11)
    if cpf == novo_cpf and not sequencia:
        print('CPF Válido')
    else:
        print('CPF inválido')
else:
    print('Digite somente NÚMEROS')
