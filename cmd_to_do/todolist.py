class ToDoList:
    def get_valid_input(prompt, validation_func):
        while True:
            user_input = input(prompt)
            if validation_func(user_input):
                return user_input
            else:
                print("Invalid input. Please try again.")
    
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        # Implement task addition logic here
        self.tasks.append(task)
        

    def view_tasks(self):
        print("\n")
        if not self.tasks:
            print("The list is empty!")
        else: 
            # Implement task viewing logic here
            for i, task in enumerate(self.tasks): 
                print(f"{i + 1}: {task}")

        
        

    def mark_completed(self, task_index):
        # Implement task completion logic here
        self.tasks[task_index] = "Completed: " + self.tasks[task_index]
        

    def remove_task(self, task_index):
        # Implement task removal logic here
        self.tasks.pop(task_index)
        

def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Quit")

        choice = ToDoList.get_valid_input("Enter your choice: ", lambda x:x)

        if choice == "1":
            task = input("Enter a task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            if not todo_list.tasks:
                print("The list is empty!")
            else:
                task_index = ToDoList.get_valid_input("Enter the task index to mark as completed: ", lambda x: x.isdigit() and 0 <= int(x) < len(todo_list.tasks))
                todo_list.mark_completed(int(task_index))
        elif choice == "4":
            if not todo_list.tasks:
                print("The list is empty!")
            
            else: 
                task_index = ToDoList.get_valid_input("Enter the task index to remove: ", lambda x: x.isdigit() and 0 <= int(x) < len(todo_list.tasks))
                todo_list.remove_task(int(task_index))
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
