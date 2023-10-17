# 1. add task
import os
from task import Task


def add_task(tasks):
    user_input = input("Enter task description:")
    task = Task(user_input)
    tasks[task.id] = task


# 2. delete task
def delete_task(tasks):
    show_tasks_with_id(tasks)
    try:
        user_input = int(input("Enter a task to delete:"))
        del tasks[user_input]
    except ValueError:
        print("Invalid input. Please enter a number.")


# 3. edit task
def edit_task(tasks: dict[Task]):
    show_tasks_with_id(tasks)
    try:
        task_id = int(input("Enter task id:"))
        if not (task_id in tasks.keys()):
            print("The task id provided doesn't exists.")
            return
        task_to_edit: Task = tasks[task_id]
        task_to_edit.change_task_description()
    except ValueError:
        print("Invalid input. Please enter a number.")


def set_task_completed():
    pass


# 4. show tasks
def show_tasks_with_id(tasks: dict[Task]):
    for key, value in tasks.items():
        print(f"{key}. {value.description}")


def display_as_todo_list(tasks: dict):
    for v in tasks.values():
        print(f"[ ] - {v.description}")
    os.system("pause")


def display_main_menu():
    print("\033c", end="\033[A")
    print("Welcome to To-do list app")
    print("=========================")
    print("Choose one of the options:")
    print("1. Add task")
    print("2. Delete task")
    print("3. Edit task")
    print("4. View tasks")
    print("0. Exit")


if __name__ == "__main__":
    tasks = {}

    user_input = ""
    while user_input != "0":
        match user_input:
            case "1":
                add_task(tasks)
            case "2":
                delete_task(tasks)
            case "3":
                edit_task(tasks)
            case "4":
                display_as_todo_list(tasks)
            case _:
                print("Please enter a valid input.")
        display_main_menu()
        user_input = input("Enter your choice:").strip()
