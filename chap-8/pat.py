'''
to generate this pattern
if n=3

***
**
*
we need to write a fn

first input the n value
start i=n , then i decrement till 1
print n times *
'''


# def pattern(n):
#     for i in range (n,0,-1):
#         print('*'*i)

# n=int(input("enter n:"))
# pattern(n)

'''
now using recursion

'''

def pattern(n):
    if n==0:
        return
    print('*'*n)
    pattern(n-1)

n=int(input("enter n:"))
pattern(n)