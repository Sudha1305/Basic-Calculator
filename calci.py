def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return "Error: Division by zero!" if b == 0 else a / b
def power(a, b): return a ** b

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Error: Please enter valid numbers.")
    exit()

print("\n--- Basic Calculator ---")
print("1. Addition (+)\n2. Subtraction (-)\n3. Multiplication (*)")
print("4. Division (/)\n5. Power (^)")

choice = input("Choose an operation (1-5): ")

if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
elif choice == '5':
    print("Result:", power(num1, num2))
else:
    print("Invalid choice.")
