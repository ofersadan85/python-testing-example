# pip install pytest


def calculate_fuel(number: int) -> int:
    return number // 3 - 2


def calculate_fuel_sum():
    with open("advent_of_code_2019_day01_numbers.txt", "r") as f:
        result = 0
        for line in f:
            number = int(line)
            result = result + calculate_fuel(number)
    return result
