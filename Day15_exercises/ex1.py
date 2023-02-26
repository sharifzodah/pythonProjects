from functions import generate_random_number

while True:

    try:
        lower = int(input("Enter the lower bound: "))
        upper = int(input("Enter the upper bound: "))
        result = generate_random_number(lower, upper)
        print(result)
    except ValueError:
        print("Wrong input! Try again.")
        continue

    user_action = input("To end the program type exit / quit: ")
    if user_action == 'exit' or user_action == 'quit':
        break
    elif len(user_action) == 0:
        continue
    else:
        print("Wrong command! Try again.")
        continue


