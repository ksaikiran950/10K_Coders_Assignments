"""✅ Built-in Functions Common to str, list, and tuple
Function	Description	Example
len()	Returns the number of items in the sequence	len("hello") → 5, len([1,2,3]) → 3
min()	Returns the smallest element	min("python") → 'h', min([3,1,4]) → 1
max()	Returns the largest element	max("python") → 'y', max((3,1,4)) → 4
sum()	Returns the sum of elements (works on numeric lists/tuples, not strings)	sum([1,2,3]) → 6
sorted()	Returns a sorted list of elements	sorted("python") → ['h','n','o','p','t','y']
any()	Returns True if any element is true	any([0,0,1]) → True, any("hi") → True
all()	Returns True if all elements are true	all([1,2,3]) → True, all("") → True
enumerate()	Returns an enumerate object (index + value)	list(enumerate("abc")) → [(0,'a'), (1,'b'), (2,'c')]
reversed()	Returns a reverse iterator	list(reversed("abc")) → ['c','b','a']
zip()	Combines two or more sequences element-wise	list(zip([1,2],[‘a’,’b’])) → [(1,'a'),(2,'b')]
🔎 Examples in Code:
s = "hello"
lst = [1, 2, 3, 4]
tup = (5, 6, 7)

print(len(s), len(lst), len(tup))        # 5, 4, 3
print(min(s), min(lst), min(tup))        # 'e', 1, 5
print(max(s), max(lst), max(tup))        # 'o', 4, 7
print(sum(lst), sum(tup))                # 10, 18

print(sorted(s))                         # ['e','h','l','l','o']
print(any(lst), all(lst))                # True, True
print(list(reversed(s)))                 # ['o','l','l','e','h']
print(list(enumerate(tup)))              # [(0,5),(1,6),(2,7)]

print(list(zip(s, lst)))                 # [('h',1),('e',2),('l',3),('l',4)]

⚡ Note:

sum() works only on numeric lists/tuples (not strings).

These functions are universal sequence functions that apply to all iterable types."""



#  2. write codes to find second largest and second smallest element in a list...

# second smallest

l=[100,10,99,9,999]
fmin=float("inf")
smin= float("inf")
for i in l:
    if i<=fmin:
        smin=fmin
        fmin=i
    elif i<smin and i>fmin:
        smin=i

print(fmin, smin)


# second largest
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
