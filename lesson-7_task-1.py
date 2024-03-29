# # Напишіть функцію, яка обчислює добуток елементів списку цілих. Список передається як параметр.
# # Отриманий результат повертається із функції.
#
import random

def multiply_elements(lst):

    result = 1  # Ініціалізуємо змінну результату зі значенням 1

    for num in lst:  # Перебираємо кожен елемент у списку
        result *= num  # Домножуємо результат на поточний елемент

    return result  # Повертаємо отриманий добуток

# Запитуємо у користувача введення п'яти випадкових чисел
numbers = []
for i in range(5):
    num = int(input(f"Введіть {i+1}-е число: "))
    numbers.append(num)

# Викликаємо функцію для обчислення добутку введених чисел
result = multiply_elements(numbers)
print("Добуток введених чисел:", result)