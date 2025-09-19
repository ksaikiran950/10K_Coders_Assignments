# 12-08-2025

# print("statement1")
# print("statement2")
# print("statement3")

# conditional statements
# depending on the condition, we can execute a block of code
# using for decision making statements

"""
1.simple if statement
2.if else statement 
3.if elif else statement
4.nested if statement"""

# 1. simple if statement
# if condition:
#     # block of code to be executed if condition is true
#     print("Condition is true, executing block of code")
# if True:
#     print("This will always execute because the condition is True")
# if False:
#     print("This will never execute because the condition is False")

# if not True:
#     print("This will never execute because the condition is False")
# print("This will always execute because the condition is True")

# money = 550
# ticket_cost_war2=295
# ticket_cost_coolie=350
# ticket_cost_kingdom = 200

# if money >= ticket_cost_war2:
#     print("You can buy a ticket for War2")
# if money >= ticket_cost_coolie:
#     print("You can buy a ticket for Coolie")
# if money >= ticket_cost_kingdom:
#     print("You can buy a ticket for Kingdom")

# if we want to execute something else when condition is fail, then we can use else
# 2. if else statement
# if condition:
#     # block of code to be executed if condition is true
#     print("Condition is true, executing block of code")
# else:
#     # block of code to be executed if condition is false
#     print("Condition is false, executing else block of code")

# if executes when the condition is true, else executes when the condition is false
# no need to give condition to else

# def P_or_F(name,eamcet):
#     if eamcet:
#         print(f"{name} is eligible for B Tech admission")
#     else:
#         print(f"{name} is not eligible for admission")
# P_or_F("sai",True)
# P_or_F("kiran",False)
# P_or_F("Ram",True)


# 1 = 0001
# 2 = 0010
# 3 = 0011
# 4 = 0100
# 5 = 0101
# 6 = 0110
# 7 = 0111
# 8 = 1000
# 9 = 1001
# 10 = 1010

# def check_even_odd(number):
#     if number % 2 == 0:
#         print(f"{number} is even")
#     else:
#         print(f"{number} is odd")
# check_even_odd(10)
# check_even_odd(15)

# def check_even_odd(number):
#     if number & 1 == 0:
#         print(f"{number} is even")
#     else:
#         print(f"{number} is odd")
# check_even_odd(10)
# check_even_odd(15)

# def check_even_odd(number):
#     last_digit = number % 10
#     if str(last_digit) in "02468":  # Check if last digit is even
#         print(f"{number} is even")
#     else:
#         print(f"{number} is odd")
# check_even_odd(10)
# check_even_odd(15)

# def check_even_odd(number):
#     last_digit = number % 10
#     if last_digit in [0, 2, 4, 6, 8]:  # Check if last digit is even
#         print(f"{number} is even")
#     else:
#         print(f"{number} is odd")
# check_even_odd(10)
# check_even_odd(15)

# 3. if elif else statement
# when we have multiple conditions to check, we can use if elif else statement
# if condition1 fails, then it will check condition2, if that fails, it will check condition3 and so on
# if all conditions fail, then it will execute else block
# if condition1:
#     # block of code to be executed if condition1 is true
#     print("Condition1 is true, executing block of code")
# elif condition2:
#     # block of code to be executed if condition2 is true
#     print("Condition2 is true, executing block of code")
# elif condition3:
#     # block of code to be executed if condition3 is true
#     print("Condition3 is true, executing block of code")
# else:
#     # block of code to be executed if all conditions are false


# def check_eamcet_rank(eamcet_rank):
#     if eamcet_rank < 10000:
#         print("You are eligible for free seat")
#     elif eamcet_rank < 20000:
#         print("You can get seat in top 10 colleges")
#     elif eamcet_rank < 30000:
#         print("You can get seat in top 20 colleges")
#     elif eamcet_rank < 80000:
#         print("You can get seat in autonomous colleges")
#     else:
#         print("You can get seat in private colleges")
# check_eamcet_rank(5000)
# check_eamcet_rank(15000)
# check_eamcet_rank(25000)
# check_eamcet_rank(150000)

# terinary
# 
# Nested if 
# last_match=True
# tot_matches=14
# run_rate=1
# team="SRh"


# def ipl():
#     if last_match ==True:
#         if tot_matches>=7:
#             if run_rate >=0.75:
#                 print(f'{team} is qualified to playoffs')
#             else:
#                 print(team,"not qualified")
#         else:
#             print("")
#     else:
#         print("team lost the match")
# ipl()


# terinory operator
# it is also known as conditional operatoor
# it is used to write the if-else in shorthand form in single line
# with this we can assign values to a variable conditionally
# we will use this only for simple and short require ment purpose only
# syntax -->  True statement if True else False statement

# print("True statement") if True else print("False Statement")

# user=input()
# pas= input()
# print("suceess") if user and pas else print("Fail")

# marks=35 
# grade="P" if marks>35 else "F"
# print(grade)

