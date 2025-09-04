'''
sum of n natural numbers , n=4 , 1+2+3+4=10

so form an equation , we get the value of n , to calcutate the sum , the n need to be decremented and added , in recursion there should be  a return base case and that is , if n=1 return 1 ? then it will solve the recursion block right, and the recursion login is sum=n+sum(n-1) 
'''

def sumofn(n):
    if n==1:
        return 1
    else:
        return n + sumofn(n-1)
n=int(input("enter a number to finf the sum of n natural numbers: "))
print(f"the sum of n natural numbers is {sumofn(n)}")


