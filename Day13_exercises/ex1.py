def get_age(year_of_birth, current_year=2023):
    return current_year-year_of_birth


birth = int(input('What is your year of birth? '))
age = get_age(birth)
if age >= 120:
    print('You are long-liver.')
else:
    print(f'You are {age} years old.')
