with open("file1.txt") as f:
    content1=f.read()
with open("poems.txt")as f:
    content2=f.read()

if content1==content2:
    print("yes files are identical")
else:
    print("fiels are not identical")
