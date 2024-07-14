from typing import Callable
import re


def generator_numbers(text: str):
    pattern = r"\d+\.\d+"
    matches = re.findall(pattern, text)
    for match in matches:
        yield float(match)


def sum_profit(text: str, func: Callable):
    gens = func(text)
    summa = 0
    for g in gens:
        summa += g
    return summa


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів 1000.00."

if __name__ == "__main__":
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
