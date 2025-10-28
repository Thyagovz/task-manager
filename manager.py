def add_task(tasks, task_name):
    task = {"tarefa": task_name, "completada": False}
    tasks.append(task)
    print(f"Tarefa {task_name} foi adicionada com sucesso!")
    return


def show_tasks(tasks):
    print("\nLista de tarefas:")
    for index, task in enumerate(tasks, start=1):
        status = "✔" if task["completada"] else " "
        task_name = task["tarefa"]
        print(f"{index}.[{status}] {task_name}")


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
    elif choose == "2":
        show_tasks(tasks)
    elif choose == "6":
        break

    print("Programa Finalizado")
