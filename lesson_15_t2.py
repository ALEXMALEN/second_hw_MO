from math import gcd


class Fraction:
    def __init__(self, a, b):
        if b == 0:  # перевірка на нульовий знаменник
            raise ValueError("Знаменник не може бути нульовим")  # викидаємо помилку
        self.a = a  # чисельник
        self.b = b  # знаменник
        self.reduce()  # спрощення дробу при ініціалізації

    def reduce(self):  # метод для спрощення дробу
        common = gcd(self.a, self.b)  # знаходження найбільшого спільного дільника
        self.a //= common  # спрощення чисельника
        self.b //= common  # спрощення знаменника

    def __mul__(self, other):
        return Fraction(self.a * other.a, self.b * other.b)  # повертаємо новий дріб

    def __add__(self, other):
        common_denominator = self.b * other.b  # спільний знаменник
        new_numerator = (self.a * other.b) + (other.a * self.b)  # новий чисельник
        return Fraction(new_numerator, common_denominator)  # повертаємо новий дріб

    def __sub__(self, other):
        common_denominator = self.b * other.b  # спільний знаменник
        new_numerator = (self.a * other.b) - (other.a * self.b)  # новий чисельник
        return Fraction(new_numerator, common_denominator)  # повертаємо новий дріб

    def __eq__(self, other):
        return self.a * other.b == other.a * self.b  # перевіряємо рівність

    def __gt__(self, other):
        return self.a * other.b > other.a * self.b  # перевіряємо більше

    def __lt__(self, other):
        return self.a * other.b < other.a * self.b  # перевіряємо менше

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"



f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 7, 6'

f_d = f_b * f_a
assert str(f_d) == 'Fraction: 1, 3'

f_e = f_a - f_b
assert str(f_e) == 'Fraction: 1, 6'

assert f_d < f_c
assert f_d > f_e
assert f_a != f_b

f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2

print('OK')
