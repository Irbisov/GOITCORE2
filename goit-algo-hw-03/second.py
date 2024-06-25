import random


def get_numbers_ticket(min_f, max_f, quantity_f):
    ls = []
    if quantity_f >= max_f or min_f < 1 or max_f > 1000:
        return f"Incorrect input  min = {min_f} or max = {max_f} or quantity = {quantity_f}. Try to change the input data."
    else:
        for i in range(quantity_f):
            target = random.randint(min_f, max_f)
            while target in ls:
                target = random.randint(min_f, max_f)
            ls.append(target)
        return ls


print(get_numbers_ticket(1, 100, 101))

"""Друге завдання


Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному квитку з числами, що випали випадковим чином і в певному діапазоні під час чергового тиражу. Наприклад, необхідно вгадати шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.


Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей.


Вона буде повертати випадковий набір чисел у межах заданих параметрів, причому всі випадкові числа в наборі повинні бути унікальні.


Вимоги до завдання:


    Параметри функції:

    min - мінімальне можливе число у наборі (не менше 1).
    max - максимальне можливе число у наборі (не більше 1000).
    quantity - кількість чисел, які потрібно вибрати (значення між min і max).

    Функція генерує вказану кількість унікальних чисел у заданому діапазоні.
    Функція повертає список випадково вибраних, відсортованих чисел. Числа в наборі не повинні повторюватися. Якщо параметри не відповідають заданим обмеженням, функція повертає пустий список.


Рекомендації для виконання:


    Переконайтеся, що вхідні параметри відповідають заданим обмеженням.
    Використовуйте модуль random для генерації випадкових чисел.
    Використовуйте множину або інший механізм для забезпечення унікальності чисел.
    Пам'ятайте, що функція get_numbers_ticket повертає відсортований список унікальних чисел.


Критерії оцінювання:


    Валідність вхідних даних: функція повинна перевіряти коректність параметрів.
    Унікальність результату: усі числа у видачі повинні бути унікальними.
    Відповідність вимогам: результат має бути у вигляді відсортованого списку.
    Читабельність коду: код має бути чистим і добре документованим.


Приклад: Припустимо, вам потрібно вибрати 6 унікальних чисел для лотерейного квитка, де числа повинні бути у діапазоні від 1 до 49. Ви можете використати вашу функцію так:


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)


Цей код викликає функцію get_numbers_ticket з параметрами min=1, max=49 та quantity=6. В результаті ви отримаєте список з 6 випадковими, унікальними та відсортованими числами, наприклад, [4, 15, 23, 28, 37, 45]. Кожен раз при виклику функції ви отримуватимете різний набір чисел.


"""
