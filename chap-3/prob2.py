name=input("enter you name: ")
uname=input("enter you username: ")

name=name.strip()
clean_name= ''
for c in name: 
    if c.isalpha() or c=='':
        clean_name+=c

words=clean_name.split()
clean_name=' '.join(words).title()
print(clean_name)

