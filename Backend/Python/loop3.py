# num=123
# while num>0:
#     d=num%10
#     print(d)
#     num//=10

# palindrome
# num=12521

# print(num)
# t=num
# rev=0
# while num>0:
#     d=num%10
#     rev=rev*10+d
#     num//=10
# print(rev)  # revre

# if rev==t:
#     print("palindrome")
# else:
#     print("Not Palindrome")

# sum of digits in a number
# num=123
# digit_sum=0
# while num>0:
#     digit_sum+=num%10
#     num//=10
# print(digit_sum)
 

# find the length of given number  without converting into string

# num=123
# count=0
# while num>0:
#     count+=1
#     num//=10    
# print(count)

# sum of only even num in given ip
ip=1234
sum=0
while ip>0:
    d=ip%10
    if d%2==0:
        sum+=d
    ip//=10
print(sum)

# count only odd num in given input
num=234567

count=0
while num>0:
    d=num%10
    if d%2 != 0:
        count+=1
    num//=10    
print(count)
# Armstrong number
# n=153
# num=n
# count=0
# while num>0:
#     count+=1
#     num//=10    
# print(count)
