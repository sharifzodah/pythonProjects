def get_listSize(input_list):
    return len(input_list.split(','))


names = input('Enter names separated by commas (no spaces): ')
print(get_listSize(names))
