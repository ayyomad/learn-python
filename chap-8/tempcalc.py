def tempcalc(f):
    return (f-32)*5/9

f=int(input("enter the temp in Fahrenheit: "))
c=tempcalc(f)
print(f"{round(c, 2)}deg C")

