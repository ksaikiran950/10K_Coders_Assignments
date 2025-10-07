#1. Basic Built-in Number Functions

#These are functions in Python that directly work with numbers without needing imports.

# abs() → returns absolute value
print(abs(-15))   # Output: 15

# round() → rounds a number to nearest integer (or given decimal places)
print(round(3.456))        # Output: 3
print(round(3.456, 2))     # Output: 3.46

# pow() → returns x raised to the power y
print(pow(2, 3))   # Output: 8

# divmod() → returns (quotient, remainder) as a tuple
print(divmod(17, 5))  # Output: (3, 2)

# max() and min() → return largest and smallest values
print(max(4, 9, 1, 6))  # Output: 9
print(min(4, 9, 1, 6))  # Output: 1

#2. Type Checking Methods

#Used to verify or convert data types in Python.

# type() → returns the type of a variable
x = 10
print(type(x))  # Output: <class 'int'>

# isinstance() → checks if a variable is of a given type
print(isinstance(x, int))       # Output: True
print(isinstance(x, float))     # Output: False

# id() → returns unique identity (memory address) of an object
print(id(x))

# Conversion functions
print(float(5))     # int → float → 5.0
print(int(3.99))    # float → int → 3
print(str(25))      # int → str → "25"

# 3. Math Module Methods

#The math module provides advanced mathematical functions.
#(Need to import math before using.)

import math

# sqrt() → square root
print(math.sqrt(25))  # Output: 5.0

# factorial()
print(math.factorial(5))  # Output: 120

# ceil() and floor()
print(math.ceil(3.2))   # Output: 4
print(math.floor(3.8))  # Output: 3

# pi and e constants
print(math.pi)  # Output: 3.141592653589793
print(math.e)   # Output: 2.718281828459045

# trigonometric functions
print(math.sin(math.pi / 2))  # Output: 1.0
print(math.cos(0))            # Output: 1.0
print(math.tan(math.pi / 4))  # Output: 1.0

# log() → natural log (base e)
print(math.log(10))        # Output: 2.302585...

# log10() → logarithm base 10
print(math.log10(100))     # Output: 2.0