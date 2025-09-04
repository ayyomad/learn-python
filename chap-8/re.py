def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)

n=int(input("enter a number you want to find factorial of: "))
print("factorial of this number is:",fact(n))