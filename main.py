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
##
day_number = int(input("Enter the day number (1-7): "))

days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

if 1 <= day_number <= 7:
    day_name = days[day_number]
    print(f"Day name: {day_name}")
else:
    print("Invalid day number. Enter a number from 1 to 7.")

