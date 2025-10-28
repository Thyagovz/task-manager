def add_task(tasks, task_name):
    task = {"tarefa": task_name, "completed": False}
    tasks.append(task)
    print(f"Tarefa {task_name} foi adicionada com sucesso!")
    return


tasks = []
while True:
    print("\nMenu do Gerenciador de Lista de tarefas:")
    print("1. Adicionar Tarefa")
    print("2. Ver Tarefas")
    print("3. Atualizar Tarefa")
    print("4. Completar Tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    choose = input("Digite a sua escolha:")

    if choose == "1":
        task_name = input("Digite o nome da tarefa que deseja adicionar: ")
        add_task(tasks, task_name)
    elif choose == "6":
        break

    print("Programa Finalizado")
