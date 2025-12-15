
# ===============================================
# SAMPLE FILE CREATION (for testing)
# ===============================================
# This creates a sample file so the program runs without error

f = open("sample.txt", "w")
f.write("Python is easy to learn. Python is powerful and easy.")
f.close()


# ===============================================
# 1. COUNT NUMBER OF WORDS IN A FILE
# ===============================================
f = open("sample.txt", "r")
data = f.read()
f.close()

words = data.split()
print("\nTotal Words:", len(words))


# ===============================================
# 2. COUNT VOWELS AND CONSONANTS IN A FILE
# ===============================================
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for ch in data:
    if ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)


# ===============================================
# 3. WORD FREQUENCY IN A FILE
# ===============================================
freq = {}

for word in words:
    word = word.lower().strip(".,")
    freq[word] = freq.get(word, 0) + 1

print("\nWord Frequencies:")
for k, v in freq.items():
    print(k, ":", v)


# ===============================================
# 4. COUNT NUMBER OF LINES IN A FILE
# ===============================================
f = open("sample.txt", "r")
lines = f.readlines()
f.close()

print("\nTotal Lines:", len(lines))


# ===============================================
# 5. COUNT NUMBER OF CHARACTERS (excluding spaces)
# ===============================================
char_count = 0
for ch in data:
    if ch != " ":
        char_count += 1

print("Characters (excluding spaces):", char_count)


# ===============================================
# 6. FIND MOST FREQUENT WORD
# ===============================================
max_word = ""
max_count = 0

for word in freq:
    if freq[word] > max_count:
        max_count = freq[word]
        max_word = word

print("Most Frequent Word:", max_word)


# ===============================================
# END OF FILE
# ===============================================
print("\nFile text analysis completed successfully.")
