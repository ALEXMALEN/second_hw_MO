def pow(x):
    return x ** 2


def some_gen(begin, end, func):
    """
    Генераторна функція  повертає по одному елементу послідовності

    begin: перший
    end: кількість  у
    func: функція, яка формує значення для послідовності
    """
    current = begin  # Початковий елемент послідовності
    for _ in range(end):  # Генеруємо 'end' елементів
        yield current  # Повертаємо поточний елемент послідовності
        current = func(current)  # Оновлюємо значення за допомогою функції


from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'

print('OK')