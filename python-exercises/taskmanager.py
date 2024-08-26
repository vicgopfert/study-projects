def exibir_lista_tarefas(all_tasks):
    if not all_tasks:
        print("Não há tarefas na lista no momento.")
    else:
        print("\n____Lista de Tarefas____")
        for key, (value, status) in all_tasks.items():
            print(f"{key} {value} - Status: {status}")

def adicionar_tarefa(all_tasks, cont_task):
    cont_task += 1
    id_task = f"{cont_task}: "
    new_task = input("Nova Tarefa: ")
    status = input("Status da Tarefa (concluído/não concluído): ").lower()
    all_tasks[id_task] = (new_task, status)
    print("Tarefa adicionada com sucesso.")
    return cont_task

def remover_tarefa(all_tasks):
    if not all_tasks:
        print("A lista de tarefas está vazia. Não há nada para remover.")
    else:
        exibir_lista_tarefas(all_tasks)
        remove_task = input("\nDigite o número da tarefa que deseja remover: ")
        task_key = remove_task + ": "
        if task_key in all_tasks:
            del all_tasks[task_key]
            print("Tarefa removida com sucesso.")
        else:
            print("Tarefa não encontrada.")

def alterar_status(all_tasks):
    if not all_tasks:
        print("A lista de tarefas está vazia. Não há nada para alterar.")
    else:
        exibir_lista_tarefas(all_tasks)
        update_task = input("\nDigite o número da tarefa que deseja alterar o status: ")
        task_key = update_task + ": "
        if task_key in all_tasks:
            new_status = input("Novo Status da Tarefa (concluído/não concluído): ").lower()
            all_tasks[task_key] = (all_tasks[task_key][0], new_status)
            print("Status da tarefa atualizado com sucesso.")
        else:
            print("Tarefa não encontrada.")

def main():
    all_tasks = {}
    cont_task = 0

    while True:
        print("\n-------Gerenciador de Tarefas-----MENU:")
        print("1: Ver Lista de Tarefas \n2: Adicionar Tarefa \n3: Remover Tarefa\n4: Alterar Status da Tarefa\n5: Sair")
        menu = input("\nDigite a opção desejada: ")
        
        if menu == '1':
            while True:
                exibir_lista_tarefas(all_tasks)
                print("\n1: Voltar ao Menu Principal")
                submenu = input("\nDigite a opção desejada: ")
                if submenu == '1':
                    break
                else:
                    print("Opção inválida. Tente novamente.")
        
        elif menu == '2':
            cont_task = adicionar_tarefa(all_tasks, cont_task)
        
        elif menu == '3':
            remover_tarefa(all_tasks)
        
        elif menu == '4':
            alterar_status(all_tasks)
        
        elif menu == '5':
            print("Saindo do Gerenciador de Tarefas...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
