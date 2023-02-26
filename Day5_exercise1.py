filenames = ['document', 'report', 'presentation']
for i, j in enumerate(filenames):
    print(f'{i}-{j.capitalize()}.txt')
print('===============================================')

ips = ['100.122.133.105', '100.122.133.111']
for i, j in enumerate(ips):
    print(f'{i+1}.IP: {j}')
selection = input("Enter the number of the IP you want: ")
print(ips[int(selection)-1])
