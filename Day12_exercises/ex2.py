def check_password(password):
    pass_options = {'strong': 'Strong password', 'weak': 'Weak password'}
    if len(password) >= 8:
        length = True
    else:
        return pass_options.get('weak')
    while length:
        digit = False
        uppercase = False
        for i in password:
            if i.isdigit():
                digit = True
            if i.isupper():
                uppercase = True

        if digit and uppercase:
            return pass_options.get('strong')
        else:
            return pass_options.get('weak')


pass_input = input('Enter password: ')
output_res = check_password(pass_input)
print(output_res)
