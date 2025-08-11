def todo_list():
    tasks = []
    while True:
        print("\n1. Добавить задачу\n2. Показать задачи\n3. Удалить задачу\n4. Выход")
        choice = input("Выберите действие (1-4): ")

        if choice == '1':
            task = input("Введите задачу: ")
            tasks.append(task)
            print("Задача добавлена!")
        elif choice == '2':
            if tasks:
                print("Ваши задачи:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("Список задач пуст!")
        elif choice == '3':
            try:
                index = int(input("Введите номер задачи для удаления: ")) - 1
                if 0 <= index < len(tasks):
                    print(f"Удалена задача: {tasks.pop(index)}")
                else:
                    print("Неверный номер!")
            except ValueError:
                print("Введите корректное число!")
        elif choice == '4':
            print("До свидания!")
            break
        else:
            print("Неверный выбор!")


todo_list()
