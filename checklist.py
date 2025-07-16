import os
import json
from task import Task

class Checklist:
    def __init__(self, filename='shabbat_checklist.txt'):
        self.filename = filename
        self.tasks = []

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(item) for item in data]
        else:
            self.tasks = [Task(desc) for desc in [
                "Buy challah",
                "Cook cholent",
                "Light candles",
                "Set the table",
                "Turn off phone"
            ]]

    def save(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump([task.to_dict() for task in self.tasks], f, ensure_ascii=False, indent=2)

    def add_task(self, description):
        self.tasks.append(Task(description))

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            return self.tasks.pop(index)
        return None

    def mark_task_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()

    def print_tasks(self):
        print("\n📋 Shabbat Preparation Checklist:")
        for i, task in enumerate(self.tasks, 1):
            status = "✔️" if task.done else "❌"
            print(f"{i}. {task.description} {status}")
        print()