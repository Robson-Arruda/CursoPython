print('')
print('Esse é um programa simples de perguntas e respostas com cálculo de nota')
print('')
perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '3',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 5x5? ',
        'respostas': {
            'a': '15',
            'b': '20',
            'c': '25',
        },
        'resposta_certa': 'c',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 50/2? ',
        'respostas': {
            'a': '25',
            'b': '20',
            'c': '27',
        },
        'resposta_certa': 'a',
    },
}
respostas_corretas = 0

for chave_p, valor_p in perguntas.items():
    print(f'{chave_p}: {valor_p["pergunta"]}')
    for chave_r, valor_r in valor_p['respostas'].items():
        print(f'[{chave_r}]: {valor_r}')
    resposta_usuario = input('Sua Resposta: ')
    resposta_usuario = resposta_usuario.lower()
    print('')
    if resposta_usuario.isnumeric():
        print('ATENÇÃO, DIGITE A LETRA CORRESPONDENTE A RESPOSTA CORRETA')
        print('')
    if valor_p['resposta_certa'] == resposta_usuario:
        print('*** Acertou ***')
        print('')
        respostas_corretas += 1
    else:
        print('*** Errou ***')
        print('')

nota = 10 / len(perguntas) * respostas_corretas

print(f'Sua nota é {nota:.2f}')
