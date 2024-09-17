from inspect import isgenerator


def pow(x):
    return x ** 2


def some_gen(begin, end, func):
    """
    begin: перший елемент послідовності
    end: кількість елементів у послідовності
    func: функція, яка формує значення для послідовності
    """
    current = begin  # Початковий елемент послідовності
    for _ in range(end):  # Цикл для обмеження кількості елементів до end
        yield current  # Повертаємо поточний елемент послідовності
        current = func(current)  # Оновлюємо поточний елемент


gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test 1'
assert list(gen) == [2, 4, 16, 256], 'Test 2'
print('Tests passed successfully!')
