import os
import shutil

caminho_original = input('Digite o caminho de origem dos aquivos: ')
caminho_novo = input('Digite o caminho para onde os arquivos serão movidos: ')

# MOVENDO

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe.')

for raiz, diretorios, arquivos in os.walk(caminho_original):
    for arquivo in arquivos:
        old_file_path = os.path.join(raiz, arquivo)
        new_file_path = os.path.join(caminho_novo, arquivo)

        shutil.move(old_file_path, new_file_path)
        print(f'Arquivo {arquivo} movido com sucesso')

# Copiando

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe.')

for raiz, diretorios, arquivos in os.walk(caminho_original):
    for arquivo in arquivos:
        old_file_path = os.path.join(raiz, arquivo)
        new_file_path = os.path.join(caminho_novo, arquivo)

        shutil.copy(old_file_path, new_file_path)
        print(f'Arquivo {arquivo} movido com sucesso')

# Apagando

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe.')

for raiz, diretorios, arquivos in os.walk(caminho_novo):
    for arquivo in arquivos:
        old_file_path = os.path.join(raiz, arquivo)
        new_file_path = os.path.join(caminho_novo, arquivo)

        os.remove(new_file_path)
        print(f'Arquivo {arquivo} apagado com sucesso.')
