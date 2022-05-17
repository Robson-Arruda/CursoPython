try:
    a = {1}
    print(a)
except NameError as erro: # Melhor prática é tratar possiveis erros
    print(erro, 'Erro do Desenvolvedor, fale com ele')

except(IndexError, KeyError) as erro:
    print('Erro de índice ou chave')

except Exception as erro:  # Para tratar erros inesperados
    print('erro inesperado')

else:
    print('Seu codigo foi executado com sucesso!!!')
finally:
    print('Finalmente')
print('Continua...')
