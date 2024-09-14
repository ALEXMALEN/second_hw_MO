import re

def validate_home_phone(phone_number):
    """
    Валідація домашнього номера телефону.

    Параметри:
    phone_number (str): Номер телефону для перевірки.

    Повертає:
    bool: True, якщо номер телефону вірний, інакше False.
    """
    return bool(re.fullmatch(r'\d{7,}', phone_number))  # Перевіряємо, чи складається номер з 7 або більше цифр

def validate_mobile_phone(phone_number):
    """
    Валідація мобільного номера телефону.

    Параметри:
    phone_number (str): Номер телефону для перевірки.

    Повертає:
    bool: True, якщо номер телефону вірний, інакше False.
    """
    return bool(re.fullmatch(r'\+?\d{10,}', phone_number))  # Перевіряємо, чи складається номер з 10 або більше цифр, можлива наявність плюса

def validate_email(email):
    """
    Валідація електронної пошти.

    Параметри:
    email (str): Email-адреса для перевірки.

    Повертає:
    bool: True, якщо email вірний, інакше False.
    """
    return bool(re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email))  # Перевіряємо, чи відповідає email-адреса шаблону

def validate_full_name(name):
    """
    Валідація ПІБ клієнта.

    Параметри:
    name (str): ПІБ клієнта для перевірки.

    Повертає:
    bool: True, якщо ПІБ вірний, інакше False.
    """
    return bool(re.fullmatch(r'[A-Za-z]{2,20}\s[A-Za-z]{2,20}\s[A-Za-z]{2,20}', name))  # Перевіряємо, чи відповідає ПІБ шаблону

# Приклади використання:
print(validate_home_phone('1234567'))  # True
print(validate_home_phone('123456'))   # False

print(validate_mobile_phone('+1234567890'))  # True
print(validate_mobile_phone('1234567890'))   # True
print(validate_mobile_phone('+12345'))       # False

print(validate_email('example@gmail.com'))  # True
print(validate_email('invalid_email.com'))  # False

print(validate_full_name('John Doe'))        # True
print(validate_full_name('Jane'))            # False