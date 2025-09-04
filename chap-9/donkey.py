word="donkey"
with open ("fl.txt","r") as f:
    content=f.read()

contentnew=content.replace("donkey","******")

with open("fl.txt","w")as f:
    f.write(contentnew)


