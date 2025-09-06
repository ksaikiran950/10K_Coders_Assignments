# find largest and second largest from given list of numbers.

l=[34,43,54,73,34,2,75,3,65,76,100]
mmax=float("-inf")
smax=float("-inf")

for i in range(len(l)):
    if l[i]>mmax:
        smax=mmax
        mmax=l[i]
    elif l[i]>smax and l[i] < mmax:
        smax=l[i]

print(mmax)
print(smax)



"""ip=['sravani','sravan','kumar','kumari','lalitha','lalith','arjun','lakshmi','nandini']
op=[(('sravani','female'),('sravan','male'),('kumar','male'))

"""

def gender(name):
    if name[-1] in "ia": #check last char is "i" or "a" 
        return (name, "female")
        
    return (name, "male")    


ip=['sravani','sravan','kumar','kumari','lalitha','lalith','arjun','lakshmi','nandini']
op = tuple(gender(name) for name in ip)
print(op)
