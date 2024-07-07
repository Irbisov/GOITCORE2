import os.path


def total_salary(path):
    if os.path.exists(path):
        with open(path) as fh:
            list_unit = fh.readlines()
            ls = [int((i.split(','))[1]) for i in list_unit]
        total = sum(ls)
        average = int(total / len(ls))
        return print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    return print(f'{path} to file is not found')


total_salary('first_example.txt')
