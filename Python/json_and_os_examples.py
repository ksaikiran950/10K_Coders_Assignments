import json
import os

# =====================================================
# JSON FILE HANDLING EXAMPLES
# =====================================================

# 1. Write data to JSON file
data = {
    "name": "Sai Kiran",
    "role": "Python Developer",
    "skills": ["Python", "SQL", "Django"]
}

f = open("user.json", "w")
json.dump(data, f)
f.close()


# 2. Read data from JSON file
f = open("user.json", "r")
content = json.load(f)
f.close()

print("\nJSON Read Data:", content)


# 3. Access specific JSON values
print("Name:", content["name"])
print("Skills:", content["skills"])


# 4. Append new key to existing JSON data
content["experience"] = "Fresher"

f = open("user.json", "w")
json.dump(content, f)
f.close()


# 5. JSON list handling
students = [
    {"name": "A", "marks": 80},
    {"name": "B", "marks": 90}
]

f = open("students.json", "w")
json.dump(students, f)
f.close()


# =====================================================
# OS MODULE EXAMPLES
# =====================================================

# 6. Get current working directory
print("\nCurrent Directory:", os.getcwd())


# 7. Create a new directory
if not os.path.exists("demo_folder"):
    os.mkdir("demo_folder")
    print("Directory created")


# 8. List files and folders in current directory
print("\nDirectory Contents:")
print(os.listdir())


# 9. Check file existence
if os.path.exists("user.json"):
    print("user.json file exists")


# 10. Rename a file
if os.path.exists("user.json"):
    os.rename("user.json", "user_data.json")
    print("File renamed")


# 11. Get file size
if os.path.exists("user_data.json"):
    print("File size:", os.path.getsize("user_data.json"), "bytes")


# 12. Delete a file
if os.path.exists("students.json"):
    os.remove("students.json")
    print("students.json deleted")


# =====================================================
# END OF FILE
# =====================================================
print("\nJSON and OS module examples executed successfully.")
