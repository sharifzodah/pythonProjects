password = input("Enter new password: ")
result = {}
if len(password) >= 8:
    result['length'] = True
else:
    result['length'] = False

digit = False
uppercase = False
for i in password:
    if i.isdigit():
        digit = True
    if i.isupper():
        uppercase = True
result['digit'] = digit
result['uppercase'] = uppercase

print(result)
if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")