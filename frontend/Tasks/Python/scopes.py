#scope:it is nothing but life/accessibility of a variable.
#we have different types of scopes:
#1.global
#2.local/function
#3.enclosed scope

# x='ramcharan'
# def tollywood():
#     print(f"{x} is accessible in tollywood")
#     x1='tillu' #x1 is having function scope/local scope

# def bollywood():
#     print(f"{x} is  accessible in bollywood")
#     # print(x1)
#     x2='ranbeer kapoor' #local scope throughout the bollywood function
#     def localwood():
#         print(f"{x} is accessible in localwood")
#         print(x2)
#         x3='sampoornesh babu' #enclosed scope
#     localwood()
#     print(x3) #cannot access outside of enclosed function
        
# tollywood()
# bollywood()

# print(f"{x} can access globally ")

#scope modifiers--->
#to chanage scope from local to global--->use global keyword
#to change scope from enclosed to local--->use nonlocal keyword


# x=50
# def demo():
#     global x #this will change the scope of x from local to global
#     x=100 #now this x is global variable
#     print(f"inside demo function x={x}")
# demo()

a=125 # global variable
def outer():
    a=12
    def inner():
        nonlocal a #this will change the scope of a from outer to inner
        a=15
        print(a,"printing inner a")
    inner()
    print(a,"printing outer a")
outer()
print(a,"printing global a")