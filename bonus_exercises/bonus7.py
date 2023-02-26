date_input = input('Enter today\'s date: ')
mood_rate = input('How do you rate your mood from 1 to 10? ') + 2 * '\n'
thought_input = input('Let your thoughts flow: ') + '\n'
with open(f'../journal/{date_input}.txt', 'w') as f:
    f.writelines(f'mood_rate: {mood_rate}')
    f.writelines(f'my_thoughts: {thought_input}')
