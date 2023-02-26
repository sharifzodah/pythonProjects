import random

BOILING_POINT = 100
FREEZING_POINT = 0
FILEPATH = 'files/todos.txt'


def get_todos(filepath=FILEPATH):
    """
    Read a text file and return the list of to-do items.
    """
    with open('files/todos.txt', 'r') as f1:
        todoList = f1.readlines()
    return todoList


def set_todos(todos_arg, filepath=FILEPATH):
    """
    Write the to-do items list in the text file.
    """
    with open('files/todos.txt', 'w') as f2:
        f2.writelines(todos_arg)


def get_state_water_temp(temperature):
    states = {'solid': 'Solid', 'liquid': 'Liquid', 'gas': 'Gas'}
    if temperature <= FREEZING_POINT:
        return states.get('solid')
    elif FREEZING_POINT < temperature < BOILING_POINT:
        return states.get('liquid')
    else:
        return states.get('gas')


if __name__ == '__main__':
    print('Hello')
    print(get_todos())

# Multiline strings:
# text = """
# Principles of productivity:
# Managing your inflow.
# Systemizing everything that repeats.
# """


def generate_random_number(lower, upper):
    result = random.randint(lower, upper)
    return result
