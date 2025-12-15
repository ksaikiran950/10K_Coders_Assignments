# =================================================
# WHAT IS random MODULE?
# =================================================
# The random module is used to generate random numbers,
# select random elements, shuffle data, and simulate
# real-world randomness like dice, OTP, games, etc.

import random


# =================================================
# 1. random.random()
# =================================================
# Returns a random float number between 0.0 and 1.0

print("\n1. random.random()")
print("Random float:", random.random())


# =================================================
# 2. random.randint(a, b)
# =================================================
# Returns a random integer between a and b (both inclusive)

print("\n2. random.randint(a, b)")
print("Random integer between 1 and 10:", random.randint(1, 10))


# =================================================
# 3. random.randrange(start, stop, step)
# =================================================
# Returns a random number from a given range

print("\n3. random.randrange(start, stop)")
print("Random number from range 0 to 50:", random.randrange(0, 50))


# =================================================
# 4. random.choice(sequence)
# =================================================
# Returns a random element from a list, tuple, or string

print("\n4. random.choice(sequence)")
colors = ["red", "blue", "green", "yellow"]
print("Random color:", random.choice(colors))


# =================================================
# 5. random.shuffle(list)
# =================================================
# Shuffles the list elements randomly (changes original list)

print("\n5. random.shuffle(list)")
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled list:", numbers)


# =================================================
# 6. random.sample(sequence, k)
# =================================================
# Returns k unique random elements from a sequence

print("\n6. random.sample(sequence, k)")
students = ["Sai", "Rahul", "Anita", "Kiran", "Neha"]
print("Random 2 students:", random.sample(students, 2))


# =================================================
# REAL-WORLD PRACTICE EXAMPLES
# =================================================

# -------------------------------------------------
# Example 1: Dice Rolling Simulation
# -------------------------------------------------
print("\nReal-World Example 1: Dice Roll")
dice = random.randint(1, 6)
print("Dice rolled:", dice)


# -------------------------------------------------
# Example 2: OTP Generator (4-digit)
# -------------------------------------------------
print("\nReal-World Example 2: OTP Generator")
otp = random.randint(1000, 9999)
print("Generated OTP:", otp)


# -------------------------------------------------
# Example 3: Lucky Winner Selector
# -------------------------------------------------
print("\nReal-World Example 3: Lucky Winner")
participants = ["A", "B", "C", "D", "E"]
winner = random.choice(participants)
print("Winner is:", winner)


# -------------------------------------------------
# Example 4: Random Password Generator (simple)
# -------------------------------------------------
print("\nReal-World Example 4: Password Generator")
chars = "abcdefghijklmnopqrstuvwxyz0123456789"
password = ""

for i in range(6):
    password += random.choice(chars)

print("Generated Password:", password)


# =================================================
# INTERVIEW QUICK NOTES
# =================================================
# random.random()   → float between 0 and 1
# random.randint() → integer range (inclusive)
# random.choice()  → single random item
# random.shuffle() → shuffle list
# random.sample()  → unique random items
#
# Note:
# random module is NOT secure for passwords/OTP in real apps.
# For security, use secrets module.

print("\nRandom module practice completed.")
