import os.path


def total_salary(path):
    if os.path.exists(path):
        with open(path) as fh:
            list_unit = fh.readlines()
        try:
            ls = [int((i.split(','))[1]) for i in list_unit]
        except IndexError:
            return print('List is out of range.')
        try:
            total = sum(ls)
            average = int(total / len(ls))
            return print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}.")
        except ZeroDivisionError:
            return print('File is empty.')
    return print(f'{path} to file is not found.')


total_salary('first_example.txt')
