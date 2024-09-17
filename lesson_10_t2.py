import re


def first_word(text):
    """ Пошук першого слова у рядку """
    # Регулярний вираз "[a-zA-Z']+" шукає перше слово:
    # - [a-zA-Z] означає пошук великих і малих літер латинського алфавіту
    #   - [a-z] шукає малі літери (від 'a' до 'z')
    #   - [A-Z] шукає великі літери (від 'A' до 'Z')
    # - ' означає, що апостроф є частиною слова, тому не буде ігноруватись (як у слові "don't")
    # - + означає, що шукаємо одну або більше літер/символів підряд, формуючи ціле слово
    match = re.search(r"[a-zA-Z']+", text)
    if match:
        return match.group(0)  # Повертаємо перше знайдене слово


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'

print('OK')