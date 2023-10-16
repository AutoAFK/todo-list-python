# 1. add task
def add_task(id_task, tasks):
    user_input = input("Enter task description:")
    tasks[id_task] = user_input


# 2. delete task
def delete_task(tasks):
    try:
        user_input = int(input("Enter a task to delete:"))
    except ValueError:
        print("Invalid input. Please enter a number.")
    del tasks[user_input]


# 3. edit task
def edit_task(tasks):
    show_tasks(tasks)
    try:
        task_id = int(input("Enter task id:"))
    except ValueError:
        print("Invalid input. Please enter a number.")
    if not (task_id in tasks):
        print("The task id provided doesn't exists.")
        return
    tasks[task_id] = input("Enter new task description:")


# 4. show tasks
def show_tasks(tasks: dict):
    for key, value in tasks.items():
        print(f"{key}. {value}")


if __name__ == "__main__":
    tasks = {}
    id_task = 1

    print("Welcome to To-do list app")
    print("=========================")
    print("Choose one of the options:")
    print("1. Add task")
    print("2. Delete task")
    print("3. Edit task")
    print("4. View tasks")
    print("0. Exit")
    user_input = input("Enter your choice:")
    while user_input != "0":
        match user_input:
            case "1":
                add_task(id_task, tasks)
                id_task += 1
            case "2":
                delete_task(tasks)
            case "3":
                edit_task(tasks)
            case "4":
                show_tasks(tasks)
            case _:
                print("Please enter a valid input.")
        user_input = input("Enter your choice:")
