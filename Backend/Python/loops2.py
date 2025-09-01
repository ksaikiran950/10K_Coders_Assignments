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

