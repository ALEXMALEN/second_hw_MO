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
    print("Incorrect operator, try again with the next operator: 'max', 'min', 'avg'.")