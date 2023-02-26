country_input = input("Enter a country: ").upper()
match country_input:
    case 'USA':
        print('Hello')
    case 'INDIA':
        print('Namaste')
    case 'GERMANY':
        print('Hallo')
    case _:
        print("No such a country in db")
