from addition_subtraction import add, subtract
from multiplication_division import multiply, divide

print("==============================")
print("       SIMPLE CALCULATOR")
print("==============================")

print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("\nChoose an operation (1-4): ")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == "1":
    result = add(a, b)

elif choice == "2":
    result = subtract(a, b)

elif choice == "3":
    result = multiply(a, b)

elif choice == "4":
    result = divide(a, b)

else:
    result = "Invalid choice"

print("\nResult:", result)
print("==============================")