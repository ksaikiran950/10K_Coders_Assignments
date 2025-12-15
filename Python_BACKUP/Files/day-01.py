# f1=open("day_01.txt","r")
# data=f1.read()

# f2=open("day-02","a+")
# for i in data:
# 	f2.write(i)
	
# f2.seek(0)
# print(f2.read())


try:
    with open("day_01.txt","r") as f:
        data=f.read()
except FileNotFoundError:
    print("Error: The file does not exists!")
else:
    print(data)
finally:
    if 'f' in locals() and f.closed==False:
        f.close()