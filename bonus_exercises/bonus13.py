print("hello")
from converter14 import convert
from parser14 import parse

height = input('Enter your height: ')
parsed = parse(height)
result = convert(parsed['feet'], parsed['inches'])
print(f'{parsed["feet"]}\' {parsed["inches"]}\" is equal to to {result} m')
if result < 1:
    print('Kid is too small for this slide.')
else:
    print('Kid can use the slide.')
