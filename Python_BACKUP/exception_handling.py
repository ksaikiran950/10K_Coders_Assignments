"""
File Name: exception_practice.py
Purpose  : Practice common Python exceptions with explanations
Author   : Practice for interviews & debugging
"""

# -------------------------------------------------
# 1. ZeroDivisionError
# -------------------------------------------------
# This error occurs when we divide a number by zero

try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")


# -------------------------------------------------
# 2. ValueError
# -------------------------------------------------
# This error occurs when conversion fails (string → int)

try:
    num = int("123a")
    print(num)
except ValueError:
    print("Error: Invalid value for integer conversion")


# -------------------------------------------------
# 3. IndexError
# -------------------------------------------------
# This error occurs when accessing an index outside list range

try:
    arr = [1, 2, 3]
    print(arr[5])
except IndexError:
    print("Error: List index out of range")


# -------------------------------------------------
# 4. KeyError
# -------------------------------------------------
# This error occurs when a dictionary key does not exist

try:
    data = {"name": "Sai", "age": 22}
    print(data["salary"])
except KeyError:
    print("Error: Key not found in dictionary")


# -------------------------------------------------
# 5. TypeError
# -------------------------------------------------
# This error occurs when incompatible data types are used together

try:
    x = "10"
    y = 5
    print(x + y)
except TypeError:
    print("Error: Cannot add string and integer")


# -------------------------------------------------
# 6. AttributeError
# -------------------------------------------------
# This error occurs when calling a method that does not exist for an object

try:
    num = 10
    print(num.upper())
except AttributeError:
    print("Error: Integer object has no attribute 'upper'")


# -------------------------------------------------
# 7. FileNotFoundError
# -------------------------------------------------
# This error occurs when trying to open a file that does not exist

try:
    file = open("data.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("Error: File not found")


# -------------------------------------------------
# 8. NameError
# -------------------------------------------------
# This error occurs when a variable is used before it is defined

try:
    print(result)
except NameError:
    print("Error: Variable is not defined")


# -------------------------------------------------
# 9. ImportError
# -------------------------------------------------
# This error occurs when importing a module that does not exist

try:
    import maths
    print(maths.sqrt(25))
except ImportError:
    print("Error: Module not found")


# -------------------------------------------------
# 10. IndentationError (EXPLANATION ONLY)
# -------------------------------------------------
# NOTE:
# IndentationError is a compile-time error.
# It cannot be caught using try-except.
#
# Example of WRONG code:
#
# if True:
# print("Hello")
#
# Correct version:
if True:
    print("Hello - indentation fixed")


# -------------------------------------------------
# End of file
# -------------------------------------------------
print("\nAll exception practice examples executed.")
