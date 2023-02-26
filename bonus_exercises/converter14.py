def convert(feet, inches):
    try:
        m = feet * 0.3048 + inches * 0.0254
        return m
    except ValueError:
        print('Invalid entry. Try again')
