def read_write_func(action):
    match action:
        case 'r':
            with open('../Day8_exercises/entries.txt') as f1:
                entry_list = f1.readlines()
                return entry_list
        case 'w':
            with open('../Day8_exercises/entries.txt', 'w') as f2:
                f2.writelines(entries)


try:
    with open('../Day8_exercises/entries.txt') as f:
        pass
except:
    with open('../Day8_exercises/entries.txt', 'w') as f:
        pass

while True:
    flip_input = input('Throw the coin and enter head or tail here: ')

    match flip_input.strip('\n'):
        case 'head' | 'tail':
            entries = read_write_func('r')
            entries.append(f'{flip_input}\n')
            read_write_func('w')
        case 'show' | 'display':
            entries = read_write_func('r')
            for index, item in enumerate(entries):
                item = item.strip('\n')
                print(f'{index + 1}.{item}')
        case _:
            break

    heads = entries.count('head\n')
    tails = entries.count('tail\n')
    heads_percentage = heads / len(entries) * 100
    tails_percentage = tails / len(entries) * 100
    print(f'Heads: {heads_percentage}%')
    print(f'Tails: {tails_percentage}%')
