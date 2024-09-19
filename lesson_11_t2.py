from inspect import isgenerator


def generate_cube_numbers(end):  # Генераторна функція яка генерує куби чисел до end включно
    num = 2  # Початкове число для якого обчислюємо куб (починаємо з 2)
    while True:  # Безкінечний цикл який працює до тих пір поки не виконається умова виходу
        cube = num ** 3  # Обчислюємо куб числа num
        if cube > end:  # Якщо куб перевищує значення end
            return  # Виходимо з генератора за допомогою return
        yield cube  # Повертаємо обчислене значення куба
        num += 1  # Збільшуємо num на 1 щоб обчислити наступний куб у наступній ітерації


gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'

print('Ok')