# Написати рекурсивну функцію, яка обчислює суму всіх чисел у діапазоні від a до b.
# Користувач вводить a та b. Проілюструйте роботу функції прикладом.
    else:
        return a + sum_range(a + 1, b)  # Рекурсивний виклик функції зі збільшенням значення початку діапазону

# Приклад використання
start = int(input("Введіть початок діапазону: "))  # Користувач вводить початок діапазону
end = int(input("Введіть кінець діапазону: "))  # Користувач вводить кінець діапазону
result = sum_range(start, end)  # Викликаємо функцію
print("Сума чисел у діапазоні від", start, "до", end, "дорівнює", result)
def sum_range(a, b): # (a) - початок діапазону, (b) - кінець діапазону

    if a > b:  # Якщо початок діапазону більше кінця, повертаємо 0
        return 0
