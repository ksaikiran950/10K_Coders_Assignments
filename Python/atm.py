class Bankaccount:
    def __init__(self,name,account_num,pin,bal=0):
        self.name=name
        self.account_num = account_num
        self.pin = pin
        self.bal = bal
    def credit(self,amount):
        for i in range(1,4):
            n=int(input("enter your pin"))
            if n==self.pin:
                if amount>0:
                    self.bal+=amount
                    print(f"Your account balance:{self.bal} ")
                else:
                    print("invalid amount entered...")
                break
            else:
                print(f"invalid pin {i} ")
        else:
            print("Too many atempts, access denied")
    def debit(self,amount):
        if amount<=self.bal and amount>0:
            self.bal-=amount
            print("debited amount",amount)
            print(f'balance: {self.bal}')
    def balance(self):
        print(f'Your account balance:{self.bal}')
    def validate(self):
        for i in range(3):
            old_pin = int(input("enter Your old pin"))
            if old_pin == self.pin:
                return True
            else:
                print("enter again")
        return False
account = Bankaccount("sai","4833",5300,10000)
print("Atm menu")
print("1.check balance")
print("2.amount debit")
print("3.amount credit")
print("4.account number")
print("5.Generate new pin")
print("6.Exit")
while True:
    n = int(input("enter your option:"))
    if n == 1:
        account.balance()
    elif n==2:
        amount = float(input("enter amount to withdraw"))
        account.debit(amount)
    elif n==3:
        amount = float(input("enter amount to deposit"))
        account.credit(amount)
    elif n==4:
        print(account.account_num)
    elif n==5:
        
        if account.validate():
            new_pin = int(input("enter your new pin"))
            account.pin = new_pin
            print("pin generated successfully")
        else:
            print("account Blocked")
            break
    elif n ==6:
        print("Thank you, good bye!")
        break
    else:
        print("Invalid option")
