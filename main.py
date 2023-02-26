from functions import *
import time

now = time.strftime('%b %d, %Y %H:%M:%S')
print('It is', now)
try:
    with open('files/todos.txt') as f:
        pass
except FileNotFoundError:
    with open('files/todos.txt', 'w') as f:
        pass

while True:
    user_actions = input("Type add, show, edit, complete or exit: ").strip()

    if user_actions.startswith('add'):
        todos = get_todos()
        todo = user_actions[len('add') + 1:]
        if len(todo) == 0:
            print('No todo added. Please try again!')
            continue
        todos.append(todo + '\n')
        set_todos(todos)

    elif user_actions.startswith('show'):
        todos = get_todos()
        # new_todos = [item.strip('\n') for item in todos] #method 1: list comprehension
        for i, item in enumerate(todos):
            item = item.strip('\n')
            print(f'{i + 1}.{item.title()}')

    elif user_actions.startswith('edit'):
        try:
            todos = get_todos()
            opt_index = int(user_actions[len('edit') + 1:]) - 1
            if opt_index > len(todos):
                print(f"There is no item with number {opt_index + 1} in the list.")
                continue
            todos[opt_index] = input("Enter a new todo: ") + '\n'
            set_todos(todos)
        except ValueError:
            print("Wrong command")
            continue

    elif user_actions.startswith('complete'):
        try:
            todos = get_todos()
            opt_index = int(user_actions[len('complete') + 1:]) - 1
            todo_to_remove = todos[opt_index].strip('\n').title()
            todos.pop(opt_index)
            set_todos(todos)
            message = f'Todo ***{todo_to_remove}*** was removed from the list.'
            print(message)
        except ValueError:
            print("Wrong command")
            continue
        except IndexError:
            print("There is no item with this number")
            continue

    elif 'exit' in user_actions:
        break
    else:
        print("Hey you entered unknown command")
