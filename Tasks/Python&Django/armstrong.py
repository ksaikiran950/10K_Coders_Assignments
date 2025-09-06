n=153
z=t=n
count=0
while t>0:
    count+=1
    t//=10
rev=0
while z>0:
    d=z%10
    rev=rev+d**count
    z//=10
print(rev)
if rev==n:
    print(f"{n} is a ArmStrong Number")
else:
    print(f'{n} is not a ArmStrong number')