"""1.


I/p:-
l1=[Sravan,harish,aravind,akhil]
l2=[24,17,20,18]


o/p:- sravan-24-Eligible
      harish-17-not eligible
      aravind-20-eligible
      akhil-18-eligible
"""
l1=["Sravan","harish","aravind","akhil"]
l2=[24,17,20,18]
l=len(l1)


for i in range(l):
    if l2[i]>=18:
        print(f"{l1[i]}-{l2[i]}-Eligible")
    else:
        print(f"{l1[i]}-{l2[i]}-Not Eligible")







"""
2.


sum of digits


I/p:- n=123          n=120
o/p:- 6   #1+2+3     3     #1+2+0
"""
n=123
tot=0
while n>0:
    tot=tot+n%10
    n//=10
print(tot)








"""3.


highest digit in an integer:-


I/p:- n=123498


o/p:- 9
"""
n=123498
hd=0
while n>0:
    d=n%10
    if  d>hd:
        hd=d
    n//=10
print(hd)





"""4.


choc_price=1/-
3 wrappers= 1 choc


amount=21     21+7+2+1==31


 how many chocs I can eat==??
"""
amt=21
cp=1
w=n=amt
while w>=3:
    e_c=w//3
    n+=e_c
    w=e_c+w%3
print(n)












