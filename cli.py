from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input('Type add, show, edit, complete or exit: ')
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]  # this is slicing the string, returns only the characters after that index
        """
        todo = input("Enter a todo: ") + "\n"

        file = open('todos.txt', 'r')
        todos = file.readlines()
        file.close()

        #with context manager
        with open("todos.txt",'r') as file:
            todos = file.readlines()
        """
        todos = get_todos()

        todos.append(todo + '\n')
        """
        file = open('todos.txt', 'w')
        file.writelines(todos)
        file.close()
        """
        write_todos(todos, "todos.txt")

    elif user_action.startswith("show"):
        """
        file = open('todos.txt', 'r')
        todos = file.readlines()
        file.close()

        with open("todos.txt", 'r') as file:
            todos = file.readlines()

        #list comprehension
        #new_todos = [item.strip('\n') for item in todos]
        # below anothe method to do the same

        new_todos = []

        for item in todos:
            new_item = item.strip('\n')
            new_todos.append(new_item)
        print(todos)
        """
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            row = f"{index + 1}.{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])

            number = number - 1
            todos = get_todos()
            """
            with open("todos.txt", 'r') as file:
                todos = file.readlines()
            """
            new_todo = input("Enter a new item: ")
            todos[number] = new_todo + '\n'

            write_todos(todos, "todos.txt")

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()
            """
            with open("todos.txt", 'r') as file:
                todos = file.readlines()
            """
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos, "todos.txt")

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)

        except IndexError:
            print("There is not item with that number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")

print("Bye!")
