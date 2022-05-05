#  Índices
#  0123456789...33
frase = 'O rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''
print(frase)
maiusculo = input('Qual letra deseja tornar maiúscula? ')

while contador < tamanho_frase:
    letra = frase[contador]
    # print(frase[contador], contador)
    # nova_string += frase[contador]
    if letra == maiusculo:
        nova_string += maiusculo.upper()
    else:
        nova_string += letra
    contador += 1
print(nova_string)
