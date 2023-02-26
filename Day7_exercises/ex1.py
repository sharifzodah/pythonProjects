names = ['john smith', 'jay santi', 'eva kuki']
names = [name.title() for name in names]
print(names)

usernames = ["john 1990", "alberta1970", "magnola2000"]
username_len = [len(i) for i in usernames]
print(username_len)

user_entries = ['10', '19.1', '20']
user_entries = [float(i) for i in user_entries]
print(user_entries)

total = sum([i for i in user_entries])
print(total)

temperatures = [10, 12, 14]
f = open('../files/temperature.txt', 'w')
f.writelines([str(i) + '\n' for i in temperatures])

numbers = [10.1, 12.3, 14.7]
numbers = [int(item) for item in numbers]
print(numbers)
