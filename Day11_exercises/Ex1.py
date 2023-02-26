def get_max_min_grades(grades):
    return f'Max: {max(grades)}, Min: {min(grades)}'


grade_list = [9.6, 9.2, 9.7]
max_min_grades = get_max_min_grades(grade_list)
print(max_min_grades)

