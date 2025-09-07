with open("this.txt") as f:
    content=f.read()
with open("this2.txt","w") as f2:
    f2.write(content)   