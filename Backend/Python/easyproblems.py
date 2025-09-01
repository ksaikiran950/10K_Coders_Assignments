# sum  of digits

n=int(input("enter number : "))

def sumofdigits(n):
    sum=0

    while n > 0:
        d = n % 10
        sum += d
        n //= 10
    return sum
print(sumofdigits(n))

