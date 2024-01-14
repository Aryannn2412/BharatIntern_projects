class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("Your to-do list:")
            for i, task in enumerate(self.tasks, 1):
                status = "✅" if task['completed'] else "❌"
                print(f"{i}. [{status}] {task['task']}")

    def mark_completed(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]['completed'] = True
            print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            del self.tasks[task_number - 1]
            print(f"Task {task_number} deleted.")
        else:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTodo List App:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_number = int(input("Enter the task number to mark as completed: "))
            todo_list.mark_completed(task_number)
        elif choice == '4':
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
