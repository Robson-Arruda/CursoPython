# Criar lista de tarefas com a opção de desfazer e refazer

def show_list(lista_tarefa):
    print('')
    print('Tarefas: ')
    print(lista_tarefa)


def add(tarefa, list_tarefa):
    list_tarefa.append(tarefa)


def desfazer(list_tarefa, memoria_tarefa):
    if not list_tarefa:
        print('Não existe tarefa para desfazer')
        return

    ultima_tarefa = list_tarefa.pop()
    memoria_tarefa.append(ultima_tarefa)


def refazer(list_tarefa, memoria_tarefa):
    if not memoria_tarefa:
        print('Não existe tarefa para Resfazer')
        return

    ultima_refazer = memoria_tarefa.pop()
    list_tarefa.append(ultima_refazer)


if __name__ == '__main__':
    list_tarefa = []
    memoria_tarefa = []

    while True:
        tarefa = input('Digite uma tarefa ou'
                       ' [desfazer, refazer ou listar]: ')
        tarefa = tarefa.lower()

        if tarefa == 'listar':
            show_list(list_tarefa)
            continue
        elif tarefa == 'desfazer':
            desfazer(list_tarefa, memoria_tarefa)
            continue
        elif tarefa == 'refazer':
            refazer(list_tarefa, memoria_tarefa)
            continue
        add(tarefa, list_tarefa)
