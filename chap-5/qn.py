# words = {
#     "sahayam": "help",
#     "kasera":"chair",
#     "ocha":"sound",
#     "amma":"mother"
# }

# word=input("enter the word you want to know: ")
# print(words[word])

# s=set()
# n=input("enter number 1: ")
# s.add(int(n))
# n=input("enter number 2: ")
# s.add(int(n))
# n=input("enter number 3: ")
# s.add(int(n))
# n=input("enter number 4: ")
# s.add(int(n))
# n=input("enter number 5: ")
# s.add(int(n))
# n=input("enter number 6: ")
# s.add(int(n))
# n=input("enter number 7: ")
# s.add(int(n))
# n=input("enter number 8: ")
# s.add(int(n))

# print(s)


# s=set()
# s.add(18)
# s.add("18")
# print(s)


di = {}

for i in range(8):
    name = input("Enter name: ")
    lang = input("Enter lang name: ")
    di[name] = lang

print(di)