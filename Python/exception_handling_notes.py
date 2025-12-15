# =================================================
# 1. WHAT IS EXCEPTION HANDLING?
# =================================================
# Exception handling is used to handle runtime errors
# so that the program does not crash unexpectedly.

# Example: Division by zero is a runtime error.


# =================================================
# 2. BASIC TRY-EXCEPT STRUCTURE
# =================================================
# try   -> code that may cause an error
# except-> code that handles the error

print("\n--- Basic Try-Except Example ---")
try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")


# =================================================
# 3. REAL-WORLD EXAMPLE 1: ATM WITHDRAWAL
# =================================================
# Logic:
# User should not withdraw more than available balance

print("\n--- ATM Withdrawal Example ---")
balance = 5000

try:
    amount = int(input("Enter withdrawal amount: "))
    if amount > balance:
        raise ValueError("Insufficient balance")
    balance -= amount
    print("Withdrawal successful")
    print("Remaining balance:", balance)
except ValueError as e:
    print("Transaction failed:", e)


# =================================================
# 4. REAL-WORLD EXAMPLE 2: LOGIN SYSTEM
# =================================================
# Logic:
# Wrong credentials should be handled safely

print("\n--- Login System Example ---")
try:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username != "admin" or password != "1234":
        raise PermissionError("Invalid credentials")

    print("Login successful")
except PermissionError as e:
    print("Login failed:", e)


# =================================================
# 5. REAL-WORLD EXAMPLE 3: STUDENT MARKS INPUT
# =================================================
# Logic:
# Marks must be numeric

print("\n--- Student Marks Example ---")
try:
    marks = int(input("Enter marks: "))
    print("Marks recorded:", marks)
except ValueError:
    print("Error: Marks should be a number")


# =================================================
# 6. MULTIPLE EXCEPT BLOCKS
# =================================================
# Different errors handled differently

print("\n--- Multiple Except Example ---")
try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print("Result:", x / y)
except ValueError:
    print("Error: Enter valid integers")
except ZeroDivisionError:
    print("Error: Division by zero not allowed")


# =================================================
# 7. ELSE BLOCK
# =================================================
# else executes only if no exception occurs

print("\n--- Else Block Example ---")
try:
    n = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
else:
    print("Valid input received:", n)


# =================================================
# 8. FINALLY BLOCK
# =================================================
# finally executes always (used for cleanup)

print("\n--- Finally Block Example ---")
try:
    file = open("sample.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("Error: File not found")
finally:
    print("File operation completed")


# =================================================
# 9. RAISING CUSTOM EXCEPTIONS
# =================================================
# Used to enforce business rules

print("\n--- Custom Exception Example ---")
try:
    age = int(input("Enter age: "))
    if age < 18:
        raise Exception("Not eligible to vote")
    print("Eligible to vote")
except Exception as e:
    print("Error:", e)


# =================================================
# 10. IMPORTANT NOTES (INTERVIEW)
# =================================================
# - Syntax errors cannot be handled
# - Exceptions occur at runtime
# - Improves program reliability
# - Used in ATM, login, APIs, file handling, DB apps

print("\nException handling notes execution completed.")
