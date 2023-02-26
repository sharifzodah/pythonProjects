def convert_liters_to_cubic_meters():
    liter = float(input('Enter container capacity in litters: '))
    try:
        volume_m3 = liter / 1000
    except ValueError:
        print('Please enter a number! ')
    return f'Volume is: {volume_m3} m3 (cubic meters)'


volume = convert_liters_to_cubic_meters()
print(volume)
