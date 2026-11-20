def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        return "ERROR: Cannot divide by zero!"
    return a / b

print("SIMPLE CALCULATOR")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter chosen operation (1 to 4): ")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == "1":
    print("SUM: ", add(a, b))
elif choice == "2":
    print("DIFFERENCE: ", subtract(a, b))
elif choice == "3":
    print("PRODUCT: ", multiply(a, b))
elif choice == "4":
    print("QUOTIENT: ", divide(a, b))
else:
    print("INVALID OPERATION")