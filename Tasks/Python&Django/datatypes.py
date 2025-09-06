# Python Data Types – Practice Tasks
# Basic Tasks (Understanding & Syntax)

 # Create 5 variables using different naming conventions (snake_case, camelCase, PascalCase, etc.).

 # snake_case
first_name = "Sai"

 # camelCase
lastName = "Kiran"

 # PascalCase
DataType="Integer"






# Try creating invalid variable names and observe the errors.
"""9variable=
 int=
 str=
 if=
 first name =
 .hello=
 """

"""
 In Python, variable names must follow specific rules. Here are examples of invalid variable names and the reasons why they are not allowed:


 9variable

 Reason: Variable names cannot start with a digit.



 total marks

 Reason: Spaces are not allowed in variable names. Use underscores (total_marks) instead.



 if

 Reason: Reserved keywords in Python cannot be used as variable names.



 S.I.

 Reason: Special characters like . are not allowed in variable names.



 #tag

 Reason: Variable names cannot start with special characters like #.



 my-variable

 Reason: Hyphens (-) are not allowed. Use underscores (my_variable) instead.



 @name

 Reason: The @ symbol is not permitted in variable names.



 Key Rules for Valid Variable Names:

 Must start with a letter (a-z, A-Z) or an underscore (_).
 Can only contain letters, digits (0-9), and underscores.
 Cannot use Python reserved keywords (e.g., if, else, while).

 By following these rules, you can ensure your variable names are valid and meaningful!
 """
'\nIn Python, variable names must follow specific rules. Here are examples of invalid variable names and the reasons why they are not allowed:\n\n\n9variable\n\nReason: Variable names cannot start with a digit.\n\n\n\ntotal marks\n\nReason: Spaces are not allowed in variable names. Use underscores (total_marks) instead.\n\n\n\nif\n\nReason: Reserved keywords in Python cannot be used as variable names.\n\n\n\nS.I.\n\nReason: Special characters like . are not allowed in variable names.\n\n\n\n#tag\n\nReason: Variable names cannot start with special characters like #.\n\n\n\nmy-variable\n\nReason: Hyphens (-) are not allowed. Use underscores (my_variable) instead.\n\n\n\n@name\n\nReason: The @ symbol is not permitted in variable names.\n\n\n\nKey Rules for Valid Variable Names:\n\nMust start with a letter (a-z, A-Z) or an underscore (_).\nCan only contain letters, digits (0-9), and underscores.\nCannot use Python reserved keywords (e.g., if, else, while).\n\nBy following these rules, you can ensure your variable names are valid and meaningful!\n'
# Create one variable of each type: int, float, str, bool. Print their type() and id().

a=2
print(type(a),id(a))
b=12.6
print(type(b),id(b))
c="sai"
print(type(c),id(c))
d=True
print(type(d),id(d))
# <class 'int'> 140713476781000
# <class 'float'> 2674924036080
# <class 'str'> 2674947788688
# <class 'bool'> 140713475895728
# 🔸 Intermediate Tasks (Manipulation & Conversion)
### 1. **List Practice**
# python
players = ["Rohit", "Virat", "Gill", "Dhoni"]
"""- Replace `"Gill"` with `"Surya"`.
- Add `"Jadeja"` at the end.
- Print the length and second last player.
"""
players[2]="Surya"
print(players)
players.append("Jadeja")
print(players)
print(len(players),players[-2])



['Rohit', 'Virat', 'Surya', 'Dhoni']
['Rohit', 'Virat', 'Surya', 'Dhoni', 'Jadeja']
# 5 Dhoni
### 2. **Tuple Practice**
laptop_info = ("HP", "16GB", "512GB SSD", 2024, True)
"""
- Try modifying one value — explain the result.
- Access and print the last 2 elements.

"""
#laptop_info[1]="8GB"  # tuple is immutable we can't modify once it is assigned
print(laptop_info)
print(laptop_info[-2],laptop_info[-1])
('HP', '16GB', '512GB SSD', 2024, True)
# 2024 True
### 3. **Set Practice**
countries = {"India", "USA", "India", "Canada", "UK", "USA"}
"""
- Print the set (observe duplicates).
- Add `"Germany"`, remove `"UK"`.
"""
print(countries)
countries.add("Germany")
print(countries)
countries.remove("UK")
print(countries)
{'USA', 'UK', 'India', 'Canada'}
{'USA', 'Germany', 'UK', 'India', 'Canada'}
{'USA', 'Germany', 'India', 'Canada'}


### **4. Frozenset Practice:**
frozen_marks = frozenset([90, 85, 75, 85])
"""
- Try to add or remove values and observe the error. 
- Print its type.
"""
print(frozen_marks)
# frozen_marks.add(45) # 'frozenset' object has no attribute 'add'
print(type(frozen_marks))



frozenset({90, 75, 85})
# <class 'frozenset'>
"""Advanced Tasks (Nesting & Real-time) 1. Dictionaries: python car_info = {”brand”: “Tesla”, “model”: “Model S”, “price”: “1.5Cr”, “features”: [“Autopilot”, “Electric”, “Sunroof”] } Add “color”: “white”
Update “price” to “1.7Cr”
Add nested key “insurance” with:
python “insurance”: { “provider”: “HDFC”, “valid_till”: “2026” } Dictionary Practice Tasks 1. Simple Dictionary Operations: python books = [ {“title”: “Atomic Habits”, “author”: “James Clear”}, {“title”: “Ikigai”, “author”: “Héctor García”}, {“title”: “Zero to One”, “author”: “Peter Thiel”}] ✅ Add a new book.
🔍 Find and print the title of the book by “Peter Thiel”.
2.      Nested Dictionary Print: python laptop = { “brand”: “Apple”, “specs”: {“ram”: “16GB”, “storage”: “1TB SSD”, “chip”: “M2”}, “price”: “2L” } 🖨️ Print “chip” value.
📝 Print: Apple laptop comes with M2 chip and costs 2L."""
car_info = {
"brand": "Tesla",
"model": "Model S",
"price": "1.5Cr",
"features": ["Autopilot", "Electric", "Sunroof"]
}
car_info["color"]="white"
print(car_info)
{'brand': 'Tesla', 'model': 'Model S', 'price': '1.5Cr', 'features': ['Autopilot', 'Electric', 'Sunroof'], 'color': 'white'}
car_info["price"]="1.7Cr"
print(car_info)
{'brand': 'Tesla', 'model': 'Model S', 'price': '1.7Cr', 'features': ['Autopilot', 'Electric', 'Sunroof'], 'color': 'white'}
car_info["insurance"]={
"provider": "HDFC",
"valid_till": "2026"
}
print(car_info)
{'brand': 'Tesla', 'model': 'Model S', 'price': '1.7Cr', 'features': ['Autopilot', 'Electric', 'Sunroof'], 'color': 'white', 'insurance': {'provider': 'HDFC', 'valid_till': '2026'}}
books = [
{"title": "Atomic Habits", "author": "James Clear"},
{"title": "Ikigai", "author": "Héctor García"},
{"title": "Zero to One", "author": "Peter Thiel"}
]
books.append({"title": "abc", "author": "xyz"})
print(books)
[{'title': 'Atomic Habits', 'author': 'James Clear'}, {'title': 'Ikigai', 'author': 'Héctor García'}, {'title': 'Zero to One', 'author': 'Peter Thiel'}, {'title': 'abc', 'author': 'xyz'}]
for book in books:
    if book["author"]=="Peter Thiel":
        print(book["title"])
# Zero to One
laptop = {
"brand": "Apple",
"specs": {"ram": "16GB", "storage": "1TB SSD", "chip": "M2"},
"price": "2L"
}
print(laptop["specs"]["chip"])
# M2
print(f"{laptop['brand']} laptop comes with {laptop['specs']['chip']} chip and costs {laptop['price']}.")
# Apple laptop comes with M2 chip and costs 2L.
"""🧩 Challenge Tasks (Think & Solve)
1. 🎬 Movie Tracker:
python

➕ Add a new show to Prime

📺 Print all shows in Netflix

2. 🧠 Memory Check:
Assign the same value to 2 variables

Print their id() — are they same?"""
ott_data = [
{"platform": "Netflix", "shows": ["Stranger Things", "Wednesday"]},
{"platform": "Prime", "shows": ["Mirzapur", "Farzi"]},
{"platform": "Hotstar", "shows": ["Special Ops", "The Freelancer"]}
]
for platform in ott_data:
    if platform["platform"] == "Prime":
        platform["shows"].append("The Boys")
print(ott_data)

# Print all shows in Netflix
for platform in ott_data:
    if platform["platform"] == "Netflix":
        print("Netflix Shows:", platform["shows"])

a=16
b=16
print(id(a))
print(id(a))
[{'platform': 'Netflix', 'shows': ['Stranger Things', 'Wednesday']}, {'platform': 'Prime', 'shows': ['Mirzapur', 'Farzi', 'The Boys']}, {'platform': 'Hotstar', 'shows': ['Special Ops', 'The Freelancer']}]
#Netflix 
# Shows: ['Stranger Things', 'Wednesday']
# 140713476781448
# 140713476781448

