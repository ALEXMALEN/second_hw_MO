num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

choice = input("Choose operator (max, min, або avg): ")

if choice == "max":
    result = max(num1, num2, num3)
    print("Maximum:", result)
elif choice == "min":
    result = min(num1, num2, num3)
    print("Minimum:", result)
elif choice == "avg":
    result = (num1 + num2 + num3) / 3
    print("Average:", result)
else:
    print("Incorrect operator, try again with the next operator: 'max', 'min', 'avg'."
###
meters = float(input("Enter meter quantity: "))

choice = input("Choose an operation (miles, inches or yards): ")

if choice == "miles":
    result = meters * 0.000621371
    print("Quantity miles: ", result)
elif choice == "inches":
    result = meters * 39.3701
    print("Quantity inches: ", result)
elif choice == "yards":
    result = meters * 1.09361
    print("Quantity yards: ", result)
else:
    print("Incorrect operation selection. Please select 'miles', 'inches' or 'yards'.")