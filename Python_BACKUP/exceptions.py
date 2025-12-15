#Compile Error
if True       # Syntax Error
    print("Hello")

def greet():
print("Hello")   # IndentationError

# Logical error
a = 10
b = 20
sum = a - b

# Runtime Errors
#ZeroDivisionError
a = 10
b = 0
print(a / b)
#Name Error
print(value)   # value is not defined
# Type Error
print(10 + "5")   # int + str
# Key Error
d = {"name": "Kiran"}
print(d["age"])   # key does not exist
# Value Error
num = int("abc")   # cannot convert
#FileNotFoundError
f = open("not_exist.txt", "r")
#AttributeError
x = 10
x.append(5)   # int has no append()


# Exception Handling
#Basic try–except
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

try:
    num = int("abc")
    result = 10 / 0
except ValueError:
    print("Invalid number!")
except ZeroDivisionError:
    print("Division by zero!")

#Using else block (runs when no error occurs)
try:
    num = int("10")
except ValueError:
    print("Invalid input!")
else:
    print("Success:", num)

# Using finally block (runs always)
try:
    f = open("data.txt")
except FileNotFoundError:
    print("File not found!")

# Catching multiple exceptions in a single block
# Clean way to handle multiple errors with one line:

except (ValueError, TypeError):
    print("Invalid input or wrong type!")

finally:
    print("Done executing.")
