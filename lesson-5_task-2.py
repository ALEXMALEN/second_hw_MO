import random

# цикл повторяется 10 раз генерируя случайное число в каждой итерации и добавляя его в список random_numbers
random_numbers = []
for _ in range(10):
    random_numbers.append(random.randint(-10, 10))

# создание списков для четных, нечетных, отрицательных, положительных чисел
even_numbers = []
odd_numbers = []
negative_numbers = []
positive_numbers = []

# цикл проходится по каждому элементу списка
for num in random_numbers:
    if num % 2 == 0:
        even_numbers.append(num)  # если число четное оно добавляется в список even_numbers
    else:
        odd_numbers.append(num)  # если число нечетное оно добавляется в список odd_numbers

    if num < 0:
        negative_numbers.append(num) # если число отрицательное оно добавляется в список negative_numbers
    elif num > 0:
        positive_numbers.append(num) # если число положительное оно добавляется в список positive_numbers

# принты для выводов всех значений
print("Original list:", random_numbers)
print("List of even numbers:", even_numbers)
print("List of odd numbers:", odd_numbers)
print("List of negative numbers:", negative_numbers)
print("List of positive numbers:", positive_numbers)