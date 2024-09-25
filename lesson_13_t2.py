class Counter:

    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

        # перевіряємо чи входить current в допустимі межі
        if not (self.min_value <= self.current <= self.max_value):
            raise ValueError(
                f"Початкове значення {self.current} повинно бути в межах [{self.min_value}, {self.max_value}]")

    def set_current(self, start):
        if self.min_value <= start <= self.max_value:  # перевіряємо допустимість нового значення
            self.current = start  # якщо допустимо оновлюємо current
        else:  # якщо нове значення виходить за межі
            raise ValueError(
                f"Значення {start} повинно бути в межах [{self.min_value}, {self.max_value}]")

    def set_max(self, max_max):
        self.max_value = max_max  # оновлюємо максимальне значення
        if self.current > self.max_value:  # якщо current перевищує новий максимум
            self.current = self.max_value  # оновлюємо current до max_value

    def set_min(self, min_min):
        self.min_value = min_min  # оновлюємо мінімальне значення
        if self.current < self.min_value:  # якщо current менше нового мінімуму
            self.current = self.min_value  # оновлюємо current до min_value

    def step_up(self):
        if self.current < self.max_value:  # якщо current менше max_value
            self.current += 1  # збільшуємо current на одиницю
        else:  # Якщо досягнуто максимального значення
            raise ValueError("Достигнуто максимального значення.")  # кидаєм виключення

    def step_down(self):
        if self.current > self.min_value:  # якщо current більше min_value
            self.current -= 1  # зменшуємо current на одиницю
        else:  # якщо досягнуто мінімального значення
            raise ValueError("Достигнуто мінімального значення.")  # кидаєм виключення

    def get_current(self):
        return self.current

    def show_valid_range(self):
        return f"Допустимі значення: від {self.min_value} до {self.max_value}"


# Основний код з перевіркою введення
try:
    min_value = 0
    max_value = 10
    print(f"Введіть початкове значення для лічильника \nДопустимі значення: від {min_value} до {max_value}.")
    user_input = input("Введіть значення : ")

    # перевіряємо чи введене значення не є порожнім і чи є воно цілим числом
    if not user_input.strip():  # перевірка на порожній ввід
        raise ValueError("Введено порожнє значення.")

    if not user_input.isdigit():  # перевірка чи є введене значення числом
        raise TypeError("Введене значення повинно бути цілим числом.")

except ValueError as e:
    print(f"Помилка: {e}")  # якщо значення не в межах або порожнє.

except TypeError as e:
    print(f"Помилка: {e}")  # якщо введено літери або спецсимволи.

print("Перевірка з домашки: ")
counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'

try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e)  # Достигнут максимум
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e)  # Достигнут минимум
assert counter.get_current() == 7, 'Test4'
