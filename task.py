from enum import Enum


class Status(Enum):
    PENDING = 1
    COMPLETED = 2


class Task:
    task_id = 1

    def __init__(self, description: str):
        self.description = description
        self.status = Status.PENDING
        self.id = Task.task_id
        Task.task_id += 1

    def change_task_description(self):
        new_description = input("Enter new description:").strip()
        self.description = new_description
