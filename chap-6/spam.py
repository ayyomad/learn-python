text=input("enter your comment: ").lower()

phrases = ["make money", "buy now", "click this", "subscribe this", "click here"]

for phrase in phrases:
    if phrase in text:
        print("spam")
        break

else:
    print("not spam")