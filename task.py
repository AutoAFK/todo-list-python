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

    def change_task_status(self):
        if self.status == Status.PENDING:
            self.status = Status.COMPLETED
        else:
            self.status = Status.PENDING
    
    def __str__(self) -> str:
        return f"{"[ ]" if self.status == Status.PENDING else "[x]"} - {self.description}"
