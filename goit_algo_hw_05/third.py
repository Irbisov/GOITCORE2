import os.path, re, collections, sys
from colorama import Fore


def load_logs(file_path: str) -> list:
    if os.path.exists(file_path):
        with open(file_path) as fh:
            list_unit = fh.readlines()
        return list_unit


def parse_log_line(line: str):
    match_dict = {}
    pattern = r"(\d+\-\d+\-\d+) (\d+\:\d+\:\d+) (\w+[A-Z]) (\w[a-zA-Z0-9_ % .]+)"
    match = re.findall(pattern, line)
    match_dict['date_log'] = match[0][0]
    match_dict['time_log'] = match[0][1]
    match_dict['name_log'] = match[0][2]
    match_dict['message_log'] = match[0][3]

    return match_dict


def filter_logs_by_level(logs: list, level: str) -> list:
    match level:
        case "INFO":
            print(f'Деталі логів для рівня {Fore.BLUE}\'INFO\':')
            ls = [i for i in logs if i['name_log'] == 'INFO']
            return ls
        case "DEBUG":
            print(f'Деталі логів для рівня {Fore.BLUE}\'DEBUG\':')
            ls = [i for i in logs if i['name_log'] == 'DEBUG']
            return ls
        case "ERROR":
            print(f'Деталі логів для рівня {Fore.RED}\'ERROR\':')
            ls = [i for i in logs if i['name_log'] == 'ERROR']
            return ls
        case "WARNING":
            print(f'Деталі логів для рівня {Fore.RED}\'WARNING\':')
            ls = [i for i in logs if i['name_log'] == 'WARNING']
            return ls
        case _:
            print('Not correct log`s name')


def count_logs_by_level(logs: list) -> dict:
    ls = []
    for i in logs:
        ls.append(i['name_log'])
    sort_ls = collections.Counter(ls)

    return dict(sort_ls)


def display_log_counts(counts: dict):
    text = (f'Рівень логування | Кількість\n'
            '-----------------|-----------\n'
            f'INFO             | {counts["INFO"]}\n'
            f'DEBUG            | {counts["DEBUG"]}\n'
            f'ERROR            | {counts["ERROR"]}\n'
            f'WARNING          | {counts["WARNING"]}')
    return text


def main():
    list_log = load_logs('log_text.txt')
    ls_log = []
    for i in list_log:
        (ls_log.append(parse_log_line(i)))
    print(display_log_counts(count_logs_by_level(ls_log)))
    try:
        if sys.argv[1] in ["INFO", "DEBUG", "ERROR", "WARNING"]:
            filtr = filter_logs_by_level(ls_log, sys.argv[1])
            ls = []
            for i in filtr:
                pattert = f'{i["date_log"]} {i["time_log"]} {i["message_log"]}\n'
                ls.append(pattert)
            return print(*ls)
        elif sys.argv[1] == 'all':
            ls = []
            for i in ls_log:
                pattert = f'{i["date_log"]} {i["time_log"]} {i["name_log"]} {i["message_log"]}\n'
                ls.append(pattert)
            return print(*ls)
        else:
            return print("Not exist command!")
    except (TypeError, ValueError, IndexError):
        return print("Some ERROR.")


"""
Вимоги до завдання:

    Скрипт повинен приймати шлях до файлу логів як аргумент командного рядка.
    Скрипт повинен приймати не обов'язковий аргумент командного рядка, після аргументу шляху до файлу логів. Він відповідає за виведення всіх записи певного рівня логування. І приймає значення відповідно до рівня логування файлу. Наприклад аргумент error виведе всі записи рівня ERROR з файлу логів.
    Скрипт має зчитувати і аналізувати лог-файл, підраховуючи кількість записів для кожного рівня логування (INFO, ERROR, DEBUG, WARNING).
    Реалізуйте функцію 

    parse_log_line(line: str) -> dict для парсингу рядків логу.
    Реалізуйте функцію load_logs(file_path: str) -> list для завантаження логів з файлу.
    Реалізуйте функцію filter_logs_by_level(logs: list, level: str) -> list для фільтрації логів за рівнем.
    Реалізуйте функцію count_logs_by_level(logs: list) -> dict для підрахунку записів за рівнем логування.
    Результати мають бути представлені у вигляді таблиці з кількістю записів для кожного рівня. Для цього реалізуйте функцію display_log_counts(counts: dict), яка форматує та виводить результати. Вона приймає результати виконання функції count_logs_by_level.


"""
if __name__ == '__main__':
    main()
