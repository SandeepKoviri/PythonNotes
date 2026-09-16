import random

def NG():
    print("----------------------------------------------------------")
    print("---------------Welcome to number gess game----------------")
    comp = random.randint(0,10)
    print("----------------------------------------------------------")
    print("---------------------Gess The Number----------------------")
    print("----------------------------------------------------------")
    user = int(input("Enter the number(0-10): "))

    if comp == user:
        
        print(f"{comp} and {user}\n U won!..........")
    else:
        print(f"{comp} and {user}\nU lost \n/'better luck next time.../'")