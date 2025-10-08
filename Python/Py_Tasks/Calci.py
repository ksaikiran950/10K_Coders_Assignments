class Calci:

    print("Choose operation: ")
    print("1. Add\n2. Sub\n3. Mul\n4. Div\n5. Rem\n6. Exit\n7. Show Name")
    
    def __init__(self, name):
        self.name = name  

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


name = input("Enter your name: ")

s1 = Calci(name)

print(f"\nHello {s1.name}! Welcome ")

while True:
    n = int(input("\nEnter your option: "))   

    if n == 1:
        a, b = map(int, input("Enter two values : ").split())
        print(s1.add(a, b))
    elif n == 2:
        a, b = map(int, input("Enter two values : ").split())
        print(s1.sub(a, b))
    elif n == 3:
        a, b = map(int, input("Enter two values : ").split())
        print(s1.mul(a, b))
    elif n == 4:
        a, b = map(int, input("Enter two values : ").split())
        print(s1.div(a, b))
    elif n == 5:
        a, b = map(int, input("Enter two values : ").split())
        print(s1.rem(a, b))    
    elif n == 6:
        print(f"Exit")
        break
    elif n == 7:
        print(f"Name: {s1.name}")
        continue
    else:
        print("Invalid choice. Please try again.")
