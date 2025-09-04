# The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score

# so first we need to generate a score and we need to similate this , so we can use a random fn
# so when an user calls the game fn it will return a highscore, if its the first time means hiscore.txt ===""then the score will be the highscore , from the next call onwards
# we will compare the score with the highscore and update the hiscore.txt file if the score is greater thatn the highscore

import random
def game():
    return random.randint(1,100)


def update_hiscore():
    with open('Hi-score.txt','r')as f:
        content=f.read().strip()
        if content=="":
            hiscore=0
        else:
            hiscore=int(content)
    

    score=game()
    print(f"your score is {score}")

    if score> hiscore:
        print("new high score")
        with open('Hi-score.txt','w')as f:
            f.write(str(score)) 
    else:
        print(f"current high score is {hiscore}")

update_hiscore()


        

