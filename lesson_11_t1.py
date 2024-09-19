from inspect import isgenerator


def is_prime(n):  # Функція для перевірки чи є число n простим
    if n < 2:  # Якщо n менше 2 воно не може бути простим
        return False  # Повертаємо False якщо n не є простим
    for i in range(2, int(n ** 0.5) + 1):  # Перебираємо всі числа від 2 до квадратного кореня з n
        if n % i == 0:  # Якщо знайдено дільник n не є простим
            return False  # Повертаємо False якщо знайдено дільник
    return True  # Якщо не знайдено дільників число n є простим


def prime_generator(end):  # Генераторна функція яка генерує прості числа до числа end
    for num in range(2, end + 1):  # Перебираємо всі числа від 2 до end включно
        if is_prime(num):  # Якщо число num є простим
            yield num  # Повертаємо (yield) це число як частину послідовності


gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'

print('Ok')