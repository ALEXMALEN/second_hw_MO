# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# num3 = float(input("Enter third number: "))
#
# choice = input("Choose operator (max, min, або avg): ")
#
# if choice == "max":
#     result = max(num1, num2, num3)
#     print("Maximum:", result)
# elif choice == "min":
#     result = min(num1, num2, num3)
#     print("Minimum:", result)
# elif choice == "avg":
#     result = (num1 + num2 + num3) / 3
#     print("Average:", result)
# else:
#     print("Incorrect operator, try again with the next operator: 'max', 'min', 'avg'.")
# ###
# meters = float(input("Enter meter quantity: "))
#
# choice = input("Choose an operation (miles, inches or yards): ")
#
# if choice == "miles":
#     result = meters * 0.000621371
#     print("Quantity miles: ", result)
# elif choice == "inches":
#     result = meters * 39.3701
#     print("Quantity inches: ", result)
# elif choice == "yards":
#     result = meters * 1.09361
#     print("Quantity yards: ", result)
# else:
#     print("Incorrect operation selection. Please select 'miles', 'inches' or 'yards'.")
#
# ### New homework!
# day_number = int(input("Enter the day number (1-7): "))
#
# days = {
#     1: "Monday",
#     2: "Tuesday",
#     3: "Wednesday",
#     4: "Thursday",
#     5: "Friday",
#     6: "Saturday",
#     7: "Sunday"
# }
#
# if 1 <= day_number <= 7:
#     day_name = days[day_number]
#     print(f"Day name: {day_name}")
# else:
#     print("Invalid day number. Enter a number from 1 to 7.")
# ###
# num1 = float(input("Enter your first number: "))
# num2 = float(input("Enter your second number: "))
#
# if num1 == num2:
#     print("Numbers is equal!")
# else:
#     print("Numbers are not equal!""\nDisplaying numbers in ascending order... ")
# if num1 < num2:
#     print(f"{num1}, {num2}")
# else:
#     print(f"{num2}, {num1}")
###
# num1 = int(input("Enter your first number: "))
# num2 = int(input("Enter you second number: "))
#
# math_calculation = input("Chose one of the following operation +    -     *      / ")
#
# if math_calculation == '+':
#     result = num1 + num2
#     print(f"Result of adding: {result}")
# elif math_calculation == '-':
#     result = num1 - num2
#     print(f"Result of subtracting: {result}")
# elif math_calculation == '*':
#     result = num1 * num2
#     print(f"Result of multiplying: {result}")
# elif math_calculation == '/':
#     if num2 != 0:
#         result = num1 / num2
#         print(f"Result of dividing: {result}")
#     else:
#         print("Error!\n""You can't divide to 0 you dumbass") # It’s not an insult, it’s just because it’s fun
# else:
#     print("Invalid mathematical operation. Enter one of the operations: + - * /")
### Homework 4, task-1
#
# input_string = input("Enter your text: ")
#
# count_digits = 0
# count_letters = 0
#
# for char in input_string:
#     if char.isalpha():
#         count_letters += 1
#     elif char.isnumeric():
#         count_digits += 1
#
# print(f"Count of letter in a string", count_digits)
# print(f"Count of number in a string", count_letters)
#
# ### Homework 4, task-2
#
# input_string = input("Enter the biggest word you heard in English: ")
# search_char = input("Enter the character to find in the text: ")
#
# count = 0
#
# for char in input_string:
#     if char == search_char:
#         count += 1
#
# print(f"The character {search_char} occurs in the {count} times.")