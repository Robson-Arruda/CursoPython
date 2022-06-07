import os
from search import formata_tamanho

caminho_procura = input('Digite o diretório se encontra o arquivo: ')
termo_procura = input('Digite o nome ou parte do nome do arquivo que deseja encontrar ou "ENTER" para buscar todos: ')
conta = 0

for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                conta += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)

                print()
                print('Encontrei o arquivo: ', arquivo)
                print('Caminho: ', caminho_completo)
                print('Nome: ', nome_arquivo)
                print('Extensão: ', ext_arquivo)
                print('Tamanho formatado: ', tamanho)
                print('Tamanho Formatado: ', formata_tamanho(tamanho))

            except PermissionError as e:
                print('Você não tem permissão para acessar esse arquivo.')
            except FileNotFoundError as e:
                print('Arquivo não encontrado.')
            except Exception as e:
                print('Erro Desconecido', e)

print()
print(f'{conta} Arquivo(s) encontrado(s).')