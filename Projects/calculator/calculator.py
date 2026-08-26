# Calculator V1

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))

print("Select an operation you would like to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operation = int(input("Enter your choice of operation (1-4): "))

if operation == 1:
    print("The result of addition is:", a + b)
elif operation == 2:
    print("The result of subtraction is:", a - b)
elif operation == 3:
    print("The result of multiplication is:", a * b)
elif operation == 4:
    if b != 0:
        print("The result of division is:", a / b)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation selected. Please choose a number between 1 and 4.")

