# st="\nmadhav is a good boy\n"
# f=open ("myfile.txt","a")
# f.write(st)
# f.close()

# with statement


with open("myfile.txt","r") as f:
    print(f.read())

# f.close()  no need to close the file when using with statement