
# loops  ...>  18/08/2025
# -----------------------------
# Example: For loop over a range
#  for
# Example: While loop with a counter
# Example: Loop through a list
# Example: Nested loops (e.g., multiplication table)
# Example: Loop with break and continue
# Add your loop examples below, each with a descriptive comme

# looping statements
# set of statements will executes multiple tiimes in a loop until a set of condition 
# to start this execution and end this execution we have to use 
# starting and ending value. this can be achieved with the help of predefined method range().

# range() will contains value, ending value and stepper(optional)

# for loop:
# for x in range():
    # stat 1
    # stat 2 
    # stat 3


# for i in range(1,11):
#     print(f'2 * {i} = {2*i}',"  ""hello world")


# for i in range(20,51):
#     if i%3==0:
#         print(i)
# print("* "*50)  
# for i in range(10,41):
#     if i%3==0 and i%5==0:
#         print(f"{i}-fizbuzz")
#     elif i%3==0:
#         print(f"{i}-fizz")
#     elif i%5==0:
#         print(f"{i}-buzz")

    



# for i in range(10,0,-1):   range(start,end,step):
#     print(i)

"""
str="fullstack"
for i in range(0,len(str),2):
    print(f'{str[i]}-hi')

print("-"*50)
str="fullstack"
for i in range(len(str)-1,-1,-1):
    print(f'{str[i]}-hi')

print("-"*50)

str="fullstack"
for i in range(len(str)-1,-1,-2):
    print(f'{str[i]}-hi')

print("-"*50)

# hello 
str='hello'
str1=''
for ch in str:
    str1=ch+str1
print(str1)

print("-"*50)
"""

# str='world'
# str1=''
# for ch in range(len(str)-1,-1,-1):
#     str1+=str[ch]
#     print(str1)

# print("-"*50)
# print(str1)
# print("-"*50)


# check weather given string is a palindrome or not using a function
# s=input()
# def palin(s):
#     str2 = ''
#     for ch in s:
#         str2 = ch + str2
#     return str2

# reversed_s = palin(s)
# if reversed_s == s:
#     print("palin")

# print numbers from 100 to 0 in reverse which are divisible by 5
# def numbers():
#     for i in range(100,-1,-1):
#         if i%5==0:
#             print(i)
# numbers()


# write a function to print tables in reverse
# n=int(input("enter a number:"))
# def table(n):
#     for i in range(10,0,-1):
#         print(f'{n} * {i} = {n*i}')
# table(n)

# whileloops

"""
for loop
it knows where to start
it knows where to stop
it knows how to update


# while (condition):
    statement1

it doesn't know where to start
it doesn't know where to stop
it doesn't know how to update

"""
# x=1
# while x<=10:
#     print(x)
#     x+=1

# str1="holiday"
# i=0
# while i<len(str1):
#     print(str1[i])
#     i+=1
"""-------------------------------------------------------------------------"""
list1=['kiran','rameshnaik','bindhu','kavya','prabhas','ramu','aravind','harish','suresh','satish']
# print("using for loop")
# for name in list1:
#     if len(name)%2==0:
#         print("Forward:",name) # forword list
#         rev=""
#         for ch in name:
#             rev = ch+rev

#         print("Reverse:",rev)
# print("_"*50)
"""-------------------------------------------------------------------------"""
# print even num length names in reverse and forward using for and while loops
# for i in range(len(list1)-1,-1,-1):
#     if len(list1[i])%2==0:
#         print("Forward:",list1[i])
#         rev=""
#         for ch in list1[i]:
#             rev =ch+rev
#         print("Backword:",rev)

# print("_"*50)
"""-------------------------------------------------------------------------"""
i=0
while i<len(list1):
    if len(list1[i])%2==0:
        print("Forword list forword names :",list1[i],end=" ")
        rev=""
        j=0
        while j<len(list1[i]):
            rev = list1[i][j]+rev
            j+=1
        print(" forword list reverse names:",rev,end="")

    i+=1
    print()
print("_"*50)
# """-------------------------------------------------------------------------"""
i=len(list1)-1
while i>=0:
    if i%2==0:
        print("reverse list Forword names:",list1[i])
        rev=""
        j=0
        while j<len(list1[i]):
            rev = list1[i][j]+rev
            j+=1
        print("reverse list reverse names:",rev)
    i-=1

print("_"*50)
# """-------------------------------------------------------------------------"""
# print numbers from 100 to 0 in reverse which are divisible by 5
def numbers():
    for i in range(100,-1,-1):
        if i%5==0:
            print(i,end=" ")
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



# list = ['harish','prabhas','sairam','kiran']
# for i in range(len(list)):
#     print(list[i])
# print("_"*50)
# for x in range(len(list)-1,-1,-1):
#     print(list[x])

# ip=['s','a','i','k','i','r','a','n']
# for ch in ip:
#     print(ch,end="_")

# print()

# print("_"*50)
# op=''
# for x in ip:
#     op=op+"_"+x
# print(op)

# print("_"*50)
# op=''
# for x in ip:
#     op=op+x+"_"
# print(op)

# print("_"*50)
# op=''
# for x in range(len(ip)-1,-1,-1):
#     op=op+ip[x]+"_"
# print(op)

# print("_"*50)

# ip=[4,3,8,9,6,7]
# small=ip[0]
# for e in ip:
#     if e<small:
#         small=e
# print(small)

# set1={'hi','hello','welcome','thing'}
# for ch in set1:
#     print(ch)

# print('_'*50)
# los=[{1,2,3},{4,5,6},{'hi','hello','world'}]
# for s in los:
#     print(s)
# print('_'*50)
# lod=[{'mv':'coolie',"language":"tamil","budget":300},
#      {'mv':'war2',"language":"hindi","budget":450},
#      {'mv':'kingdom',"language":"telugu","budget":250}
#      ]
# for x in lod:
#     print(x)
# print('_'*50)

# for x in lod:
#     if x['language']=='telugu':
#         print(x)
# print('_'*50)


# control statements

# break and continue


# break  --> will stop the entire loop at particular condition
# continue --> will skip the current iteration at particular condition.

# for x in range(1,11):
#     if x==5:
#         break
#     print(x)

# print('_'*50)
# for x in range(1,11):
#     print(x)
#     if x==5:
#         break
#     x+=1
# print('_'*50)
# for x in range(1,11):
#     x+=1
#     print(x)
#     if x==5:
#         break
# print('_'*50)
# for x in range(1,11,2):
#     x+=1
#     print(x)
#     if x==5:
#         break
# print('_'*50)
# for x in range(1,11,2):
#     print(x)
#     if x==5:
#         continue

# print('_'*50)
# for x in range(1,11,2):
#     if x==5:
#         continue
#     print(x)
    
numbers = [4, 1, 7, 3, 9]

# Selection sort in descending order
for i in range(len(numbers)):
    max_idx = i
    for j in range(i + 1, len(numbers)):
        if numbers[j] > numbers[max_idx]:
            max_idx = j
    # Swap the found maximum element with the first element
    numbers[i], numbers[max_idx] = numbers[max_idx], numbers[i]

print("Sorted list (descending):", numbers)

