user_prompt = "Enter your name: "
names = []
while True:
    name = input(user_prompt)
    if name == 'stop':
        break
    names.append(name)
    print(names)

