import os

# List files
print(os.listdir("."))

# Create folder
if not os.path.exists("backup"):
    os.mkdir("backup")

# Rename file
os.rename("old.txt", "new.txt")

# Walk through directories
for root, dirs, files in os.walk("."):
    print(root, dirs, files)

# Environment variable
os.environ["API_KEY"] = "12345"
print(os.getenv("API_KEY"))
