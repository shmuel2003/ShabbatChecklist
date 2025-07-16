from checklist import Checklist

class ChecklistApp:
    def __init__(self):
        self.checklist = Checklist()
        self.checklist.load()

    def run(self):
        while True:
            print("\n--- Menu ---")
            print("1. View checklist")
            print("2. Mark task as done")
            print("3. Add a task")
            print("4. Remove a task")
            print("5. Save and exit")

            choice = input("Choose an option (1–5): ")

            if choice == '1':
                self.checklist.print_tasks()
            elif choice == '2':
                self.mark_task()
            elif choice == '3':
                self.add_task()
            elif choice == '4':
                self.remove_task()
            elif choice == '5':
                self.checklist.save()
                print("Checklist saved. Shabbat Shalom! 🌅")
                break
            else:
                print("Invalid choice. Please try again.")

    def mark_task(self):
        self.checklist.print_tasks()
        try:
            index = int(input("Enter the task number you completed: ")) - 1
            self.checklist.mark_task_done(index)
            print("Task marked as done!")
        except ValueError:
            print("Invalid input.")

    def add_task(self):
        desc = input("Enter a new task: ").strip()
        if desc:
            self.checklist.add_task(desc)
            print("Task added.")
        else:
            print("Empty task not added.")

    def remove_task(self):
        self.checklist.print_tasks()
        try:
            index = int(input("Enter the number of the task to remove: ")) - 1
            removed = self.checklist.remove_task(index)
            if removed:
                print(f"Removed task: {removed.description}")
            else:
                print("Invalid number.")
        except ValueError:
            print("Invalid input.")