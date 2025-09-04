def greatest(a, b, c):
    if (a>b and a>c):
        return a
    elif(b>a and b>c):
        return b        
    else:
        return c   
    
a=1
b=3
c=4
print("The greatest number is:", greatest(a, b, c))