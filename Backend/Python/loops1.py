# print numbers from 100 to 0 in reverse which are divisible by 5
def numbers():
    for i in range(100,-1,-1):
        if i%5==0:
            print(i)
numbers()


# write a function to print tables in reverse
n=int(input("enter a number:"))
def table(n):
    for i in range(10,0,-1):
        print(f'{n} * {i} = {n*i}')
table(n)


# check weather given string is a palindrome or not using a function
s=input()
def palin(s):
    str2 = ''
    for ch in s:
        str2 = ch + str2
    return str2

rev = palin(s)
if rev == s:
    print("palindrome")
else:
    print("not palindrome")