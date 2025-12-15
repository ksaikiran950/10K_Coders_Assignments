

# =================================================
# 1. ATM Mini Program
# =================================================
# Features:
# - Check balance
# - Withdraw money
# - Handle invalid input and insufficient balance

balance = 5000  # Initial account balance

try:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Withdraw Money")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current Balance:", balance)

    elif choice == 2:
        amount = int(input("Enter amount to withdraw: "))

        if amount > balance:
            raise ValueError("Insufficient balance")

        balance -= amount
        print("Withdrawal successful")
        print("Remaining Balance:", balance)

    else:
        print("Invalid choice")

except ValueError as e:
    print("Error:", e)

# =================================================
# 2. Login System
# =================================================
# Features:
# - Username and password validation
# - Handles wrong credentials safely

try:
    correct_username = "admin"
    correct_password = "1234"

    username = input("\nEnter username: ")
    password = input("Enter password: ")

    if username != correct_username or password != correct_password:
        raise PermissionError("Invalid username or password")

    print("Login successful")

except PermissionError as e:
    print("Login failed:", e)

# =================================================
# 3. Calculator Program
# =================================================
# Features:
# - Basic arithmetic operations
# - Handles zero division and wrong input

try:
    print("\n--- Calculator ---")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ")

    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif op == "/":
        print("Result:", a / b)
    else:
        print("Invalid operator")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
except ValueError:
    print("Error: Please enter valid numbers")

# =================================================
# End of Program
# =================================================
print("\nProgram execution completed successfully.")
