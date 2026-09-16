import random
def RPS():
    print("Welcome to Rock, Paper, Scissors")
    choices = ["rock", "paper", "scissors"]
    u = 0
    c = 0
    i = 0
    while i < 5:
        print("Welcome to Rock, Paper, Scissors")
        print("Choose your option:\n1. Rock\n2. Paper\n3. Scissors")
        user_choice = int(input("Enter your choice (1-3): "))
        computer_choice = random.choice(choices)
        print(f"Computer chose {computer_choice}")
        if user_choice == 1 and computer_choice == "rock" or user_choice == 2 and computer_choice == "paper" or user_choice == 3 and computer_choice == "scissors":
            print("It's a tie!")
        elif user_choice == 1 and computer_choice == "scissors" or user_choice == 2 and computer_choice == "rock" or user_choice == 3 and computer_choice == "paper":
            print("You win!")
            u += 1
        else:
            print("Computer wins!")
            c += 1
        i += 1
    print("Game over!")
    print("____________________________________________")
    print(f"U won {u} times and computer won {c} times.")
    if u > c:
        print("You win the game!")
    else:
        print("Computer wins the game!")