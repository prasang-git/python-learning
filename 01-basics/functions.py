def greet(name):
    print(f"Hello, {name}! Welcome!")
greet("Prasang")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

result = subtract(10, 5)
print(result)
result = add(5, 3)
print(result)
result = multiply(4, 6)
print(result)
result = divide(10, 0)
print(result)