def read_write_todos(action):
    match action:
        case 'r':
            with open('files/todos.txt', 'r') as f1:
                todoList = f1.readlines()
                return todoList
        case 'w':
            with open('files/todos.txt', 'w') as f2:
                f2.writelines(todos)


try:
    with open('files/todos.txt') as f:
        pass
except FileNotFoundError:
    with open('files/todos.txt', 'w') as f:
        pass

while True:
    user_actions = input("Type add, show, edit, complete or exit: ").strip()
    match user_actions:
        case 'add':
            todos = read_write_todos('r')
            todo = input("Enter a todo: ") + '\n'
            todos.append(todo)
            read_write_todos('w')

        case 'show' | 'display':
            todos = read_write_todos('r')
            # new_todos = [item.strip('\n') for item in todos] #method 1: list comprehension
            for i, item in enumerate(todos):
                item = item.strip('\n')
                print(f'{i + 1}.{item.title()}')

        case 'edit':
            todos = read_write_todos('r')
            opt = int(input("Enter the number of todo to edit: ")) - 1
            todos[opt] = input("Enter a new todo: ") + '\n'
            read_write_todos('w')

        case 'complete':
            todos = read_write_todos('r')
            opt = int(input("Enter the number of todo to complete: ")) - 1
            todo_to_remove = todos[opt].strip('\n').title()
            todos.pop(opt)
            read_write_todos('w')
            message = f'Todo ***{todo_to_remove}*** was removed from the list.'
            print(message)

        case 'exit':
            break
        case _:
            print("Hey you entered unknown command")
