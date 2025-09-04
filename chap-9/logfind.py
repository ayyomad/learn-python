with open("log.txt","r") as f:
    content=f.read()

if ("python" in content.lower()):
    print("Found python")   

else: print("Not found")
