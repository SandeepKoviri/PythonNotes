import random
from Proj4_5rockPaperScissior import RPS
from proj4_chGame import NG


def playaGame():
    print("Wana play a game?")
    print("1. Yes")
    print("2. No")
    a = int(input("Enter your choice: "))
    if a == 1:
        print("____________________________________________")
        print("-----------what game u wana play------------")
        print("____________________________________________")
        print("1. Rock Paper Scissor")
        print("2. Guess the Number")
        print("3. study....")
        b = int(input("Enter your choice: "))
        if b == 1:
            RPS()
        elif b == 2:
            NG()
        else:
            print("study")
    elif a == 2:
        print("Get lost u freaking idiot")
    else:
        print("enter a valid choice")

