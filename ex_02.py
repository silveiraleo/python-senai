lista = []

while True:
    menu_op = (
        "1 - Adicionar tarefa",
        "2 - Visualizar tarefas",
        "3 - Marcar como concluída",
        "4 - Remover tarefa",
        "5 - Sair"
    )
    print('\nMenu de Opções:')
    for opcao in menu_op:
        print(opcao)

    escolha = input('Insira a opção: ')
    
    if escolha == '1':
        tarefa = input('Insira a tarefa: ')
        if tarefa:
            lista.append({'tarefa': tarefa, 'status': 'Não concluído'})
            print('Tarefa adicionada com sucesso!')
        else:
            print('Tarefa não pode estar vazia.')
    
    elif escolha == '2':
        if lista:
            print('\nTarefas:')
            for id, item in enumerate(lista, start=1):
                print(f"{id}. {item['tarefa']}: {item['status']}")
        else:
            print('Não há tarefas para exibir.')
    
    elif escolha == '3':
        tarefa_nome = input('Insira a tarefa que concluiu: ')
        for item in lista:
            if item['tarefa'] == tarefa_nome:
                item['status'] = 'Concluída'
                print('Tarefa marcada como concluída!')
                break
        else:
            print('Tarefa não encontrada.')
    
    elif escolha == '4':
        tarefa_nome = input('Insira a tarefa que deseja remover: ')
        for item in lista:
            if item['tarefa'] == tarefa_nome:
                lista.remove(item)
                print('Tarefa removida com sucesso!')
                break
        else:
            print('Tarefa não encontrada.')
    
    elif escolha == '5':
        break
    
    else:
        print('Opção inválida, tente novamente.')
