""" if a number is 152  
check weather  151 or 153 is a Armstrong Number"""

def Armstrong(n):
    z=t=n
    count=0
    while t>0:
        count+=1
        t//=10
    sum=0
    while z>0:
        sum=sum+(z%10)**count
        z//=10
    return sum==n

def beside_num(n):
    pv_num = n - 1
    nxt_num = n + 1

    print(f"Previous number {pv_num} is Armstrong?     {Armstrong(pv_num)}")
    print(f"Current number {n} is Armstrong?      {Armstrong(n)}")
    print(f"Next number {nxt_num} is Armstrong?         {Armstrong(nxt_num)}")

beside_num(152)
