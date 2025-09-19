"""Built-in List Methods in Python


Here are the methods available on list objects, what they do, and example usage:

Method	Description	Example
append(x)	Adds an item x to the end of the list. 

lst = [1,2]; lst.append(3) → lst = [1,2,3]
extend(iterable)	Adds all items from iterable to the end of the list. 

lst = [1,2]; lst.extend([3,4]) → [1,2,3,4]
insert(i, x)	Inserts x at index i. Items from i onward shift right. 

lst = [1,3]; lst.insert(1,2) → [1,2,3]
remove(x)	Removes the first occurrence of x from the list. Raises ValueError if x is not present. 

lst = [1,2,3,2]; lst.remove(2) → [1,3,2]
pop([i])	Removes and returns the item at index i. If i not provided, removes & returns the last item. Raises IndexError if list is empty or i out of range. 

lst = [1,2,3]; lst.pop() → returns 3, list becomes [1,2]
clear()	Removes all items from the list. Resulting list is empty. 

lst = [1,2,3]; lst.clear() → []
index(x[, start[, end]])	Returns the lowest index in the list where x appears between start and end. Raises ValueError if x not found. 

lst = [1,2,3,2]; lst.index(2) → 1
count(x)	Returns number of times x is in the list. 

lst = [1,2,2,3]; lst.count(2) → 2
sort(*, key=None, reverse=False)	Sorts the list in place. You can supply a key function, and/or set reverse=True. 

lst = [3,1,2]; lst.sort() → [1,2,3]
reverse()	Reverses the elements of the list in place. 

lst = [1,2,3]; lst.reverse() → [3,2,1]
copy()	Returns a shallow copy of the list. Changes to the new list won’t affect the original for top-level items (but nested objects are still shared). 

lst2 = lst.copy()

Other Useful Functions / Operations Related to Lists

These are not list methods, but built-in functions or operations often used with lists.

len(lst) — number of elements in the list. 


list(iterable) — to create a list from another iterable. 


Membership test: x in lst / x not in lst. 


Slicing (lst[start:end]) — to get sublists; also assign to slices to modify; del lst[i] or del lst[start:end] to delete. 
"""
"""
list.sort(key=len) (or generally with any key), and

list.clear().


"""
#1. Internal code for list.sort(key=len)

#👉 list.sort() in Python uses Timsort (a hybrid of merge sort + insertion sort). But simplified, you can imagine it like this:

#When you pass key=len, Python transforms each element into a tuple (key(element), element) behind the scenes (called Schwartzian transform).

#Equivalent Python-style internal code:
def my_sort(lst, key=None, reverse=False):
    # Step 1: decorate (apply key function if given)
    if key is not None:
        decorated = [(key(x), x) for x in lst]
    else:
        decorated = [(x, x) for x in lst]
    
    # Step 2: sort decorated list (using a simple algorithm here)
    decorated.sort(reverse=reverse)   # internally uses Timsort
    
    # Step 3: undecorate (extract original values in sorted order)
    for i in range(len(lst)):
        lst[i] = decorated[i][1]   # update in place


#✅ Example:

words = ["apple", "kiwi", "banana", "mango"]
my_sort(words, key=len)
print(words)   # ['kiwi', 'mango', 'apple', 'banana']


# 👉 CPython uses Timsort in C (Objects/listobject.c), but conceptually this is what happens.

#2. Internal code for list.clear()

#👉 clear() just removes all elements from the list. Internally, it resets the length to zero.

#Equivalent Python-style internal code:
def my_clear(lst):
    # One way: keep popping until empty
    while len(lst) > 0:
        lst.pop()
    # Another faster way: just reassign slice
    # lst[:] = []


#✅ Example:

nums = [1, 2, 3, 4]
my_clear(nums)
print(nums)   # []


#👉 In CPython C source, it calls list_ass_slice() to replace the full slice with an empty list (effectively same as lst[:] = []).