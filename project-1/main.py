'''
snake water gun game
1 for snake
-1 for water
0 for gun
'''
import random

computer =random.choice([-1,0,1])
youstr=input("Enter s or w or g: ")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"snake",-1:"water",0:"gun"}
you=youDict[youstr]
print(f"computer chose {reverseDict[computer]} and you chose {reverseDict[you]}")

# now cases , both same , draw means computer==you
# if computer has greater thing than you , computer wins means 1 and -1 , 0 and 1 , -1 and 0
# else you win


if computer==you:
    print("draw")
elif (computer==1 and you==-1) or (computer==0 and you==1) or (computer==-1 and you==0):
    print("computer wins")
else:
    print("you win")    