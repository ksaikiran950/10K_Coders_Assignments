class Calci:
    def __init__(self, name):
        self.name = name  

    def get_name(self):
        return self.name

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def rem(self, a, b):
        return a % b
    

name= input("enter your name: ")
s1=Calci(name)


print(f'Hi {s1.get_name}  !   Welcome')

print("Choose operation: ")
print("1. Add\n2. Sub\n3. Mul\n4. Div\n5. Rem\n6. Exit\n7. Show Name")

while True:
    n = int(input("\nEnter your option: "))

    if n == 6:
        print(f"Exit")
        break

    elif n == 7:
        print(f"Name: {s1.get_name()}")
        continue

    a, b = map(int, input("Enter two values : ").split())

    if n == 1:
        print("Result:", s1.add(a, b))
    elif n == 2:
        print("Result:", s1.sub(a, b))
    elif n == 3:
        print("Result:", s1.mul(a, b))
    elif n == 4:
        print("Result:", s1.div(a, b))
    elif n == 5:
        print("Result:", s1.rem(a, b))
    else:
        print("Invalid choice. Please try again.")


