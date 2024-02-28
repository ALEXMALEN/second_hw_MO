import random

numbers = []
arr_size = 10

for _ in range(arr_size):
    numbers.append(random.randint(-10, 10))


negative_numbers_sum = 0
even_numbers = 0
odd_numbers = 0
sum_elements_index = 0

for number in numbers:
    if number < 0:
        negative_numbers_sum += number
    if number % 2 == 0:
        even_numbers += number
    if number % 2 != 0:
        odd_numbers += number
    if number % 3 == 0:
        sum_elements_index += number

print(f"Here is a list of random numbers: {numbers}")
print(f"The sum of negative numbers: {negative_numbers_sum}")
print(f"The sum of even numbers: {even_numbers}")
print(f"The sum of odd numbers: {odd_numbers}")
print(f"The sum of elements with multiple index 3: {sum_elements_index}")

min_value_index = numbers.index(min(numbers))
max_value_index = numbers.index(max(numbers))

if min_value_index > max_value_index:
    min_value_index, max_value_index = max_value_index, min_value_index

result = 0

for i in range(min_value_index + 1, max_value_index):
    result += numbers[i]

print(f"The sum of elements between the minimum and maximum: {result}")

first_positive_index = last_positive_index = 0
for e in range(arr_size - 1, -1, -1):
    if numbers[e] > 0:
        last_positive_index = e
        break

print(f"The first positive index: ", first_positive_index, "The last positive index: ", last_positive_index)