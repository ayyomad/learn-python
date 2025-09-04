f=open("poems.txt","r")
c=f.read()
if "twinkle" in c:
    print("yes, twinkle is present")
else:
    print("no, the word twnkle isnot presetn in the file")
f.close()


