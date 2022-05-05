"""Jogo da FORCA com 10 tentativas"""

palavra = 'PARALELEPIPEDO'
digitadas = []
chances = 0
digitadas_errado = []
print(f' palavra com {len(palavra)} letras!')
while chances < 10:
    print('******')
    letra = input('Digite uma letra: ')
    letra = letra.upper()

    if letra.isdigit():
        print('Números não valem, Digite somente letras')
        print('*******')
        chances += 1
        print(f'*** você tem "{10 - chances}" chances ***')
        continue
    if len(letra) > 1:
        print('Digite Somente uma LETRA')
        print('*******')
        chances += 1
        print(f'*** você tem "{10 - chances}" chances ***')
        continue
    digitadas.append(letra)
    if letra in palavra:
        print(f'UHUUULLL a letra "{letra}" existe na palavra.')
        print('')
    else:
        print(f'IXIIIII a letra "{letra}" não existe na palavra.')
        digitadas.pop()
        digitadas_errado.append(letra)
        print('*******')
    chances += 1
    secreto_temp = ''
    for i in palavra:
        if i in digitadas:
            secreto_temp += i
        else:
            secreto_temp += '*'
    print(f'>>>>>  {secreto_temp}  <<<<<')
    print('')
    print(f'*** você tem "{10-chances}" chances ***')
    print('')
    print(f'"{digitadas_errado}", você já digitou e errou')
    if palavra == secreto_temp:
        print(f'Parabéns você ganhou!!! "{palavra}" é a palavra secreta')
        break
