def is_even(number):
    i = 0 # Починаємо з 0 і додаємо 2 поки не дійдемо до числа або перевищимо його
    while i < number:
        i += 2  # Додаємо 2 на кожному кроці
    # Якщо дійшли до числа - воно парне, якщо перевищили - непарне
    return i == number


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'