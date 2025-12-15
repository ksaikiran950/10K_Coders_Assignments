# 1. Read mode (r)
f = open("file.txt", "r")
print(f.read())
f.close()

# 2. Write mode (w)
f = open("file.txt", "w")
f.write("Hello Python")
f.close()

# 3. Append mode (a)
f = open("file.txt", "a")
f.write("\nNew Line")
f.close()

# 4. Read + Write mode (r+)
f = open("file.txt", "r+")
f.write("Start")
f.close()

# 5. Write + Read mode (w+)
f = open("file.txt", "w+")
f.write("Fresh Data")
f.close()

# 6. Append + Read mode (a+)
f = open("file.txt", "a+")
f.write("\nAppend Data")
f.close()

# 7. Binary Read mode (rb)
f = open("file.txt", "rb")
print(f.read())
f.close()

# 8. Binary Write mode (wb)
f = open("file.bin", "wb")
f.write(b"Binary Data")
f.close()

# 9. Exclusive Creation mode (x)
f = open("newfile.txt", "x")
f.write("New File")
f.close()
