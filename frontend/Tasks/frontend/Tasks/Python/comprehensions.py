#  comprehension ---> binding the data in 
# to pack multiple values  in list , tuple , dictionary or set in simole way then we can use comphrehensions

# comprehension is combination of   'operation/expression' , iteration, and conditions(optional)

# str ='welcome'

# str1={x+"-hi" for x in str }

# print(str1)

# create a list numbers from 1 to using comprehensions

# op=[x for x in range(1,11)]
# print(op)
# op=[x**2 for x in range(1,11)]
# print(op)
# op=[x for x in range(1,11,2)]
# print(op)
# op=[x for x in range(1,11) if x%2==0]
# print(op)

# if filteration is there
# Steps 1. iter
#       2. filteration
#       3. operation

# if no filteration
# 1. iteration
# 2. operation

# ip = [1,4,7,9,11,13,24,56,108,234,125]
# op=[x*2 for x in ip if x%2==0]
# print(op)
# ip=[x*2 for x in ip if x%2==0]
# print(ip)



#Create a list of factorials of the first 5 numbers  using list comprehensions.
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
op=[fact(n) for n in range(1,6) ]
print(op)