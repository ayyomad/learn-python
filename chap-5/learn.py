# dic, key value pairs , can store any type of data inside
# unorderd , indexed , mutable , cannot contain duplicate keys 


marks= {
    "madhav":12,
    "arun":22,
    "raju":32
    
}

print(marks, type(marks))
print(marks.keys())
print(marks.items())
print(marks.values())

print(marks["arun"])

marks.update({"madhav":8})
print(marks)