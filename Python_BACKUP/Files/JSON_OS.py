import json

# Write data to JSON file
data = {
    "name": "Kiran",
    "skills": ["Python", "SQL", "Django"]
}

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# Read data from JSON file
with open("data.json", "r") as f:
    info = json.load(f)

print(info)











import json

# Update JSON file
with open("data.json") as f:
    data = json.load(f)

data["skills"].append("React")

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# Handle JSON decode error
try:
    with open("wrong.json") as f:
        json.load(f)
except json.JSONDecodeError:
    print("Invalid JSON format")
