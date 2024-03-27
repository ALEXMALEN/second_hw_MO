# Напишіть функцію, яка визначає кількість простих чисел у списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.

import random


def is_prime(n):

    # Числа менші або рівні 1 не є простими
    if n <= 1:
        return False
    # Перевіряємо, чи n ділиться на будь-яке число від 2 до квадратного кореня з n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            # Якщо n ділиться без залишку, воно не просте
            return False
    # Якщо не знайдено дільників, число просте
    return True


def count_primes(numbers):

    # Використовуємо генератор списку з функцією is_prime для підрахунку простих чисел
    return sum(is_prime(num) for num in numbers)


# Створюємо список з 10 випадкових чисел в діапазоні від 1 до 100
random_numbers = [random.randint(1, 100) for _ in range(10)]

# Виводимо згенерований список чисел
print("Випадково згенерований список чисел:", random_numbers)
# Виводимо кількість простих чисел, використовуючи функцію count_primes
print("Кількість простих чисел у списку:", count_primes(random_numbers))