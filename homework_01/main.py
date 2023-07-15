"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*nums):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [num ** 2 for num in nums]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(n):
    if n == 1:
        return False
    if n > 1:
        count = 0
        for num in range(1, int(n ** 0.5)+1):
            if n % num == 0:
                count +=1
        if count == 1:
            return True

def filter_numbers(numbers, type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if type == ODD:
        return list(filter(lambda number: number % 2 != 0, numbers))
    if type == EVEN:
        return list(filter(lambda number: number % 2 == 0, numbers))
    if type == PRIME:
        return list(filter(is_prime, numbers))
