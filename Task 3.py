import random
print("Welcome to Rock Paper Scissor Game")
Game="Start"
while (Game.lower()!="exit"):
    print("1. rock")
    print("2. paper")
    print("3. scissor")
    print()
    user = input("Enter your choice (rock, paper, scissor) or type 'Exit' to stop the game: ").lower()
    lst=["rock","paper","scissor"]
    computer=random.choice(lst)
    if user not in ["rock", "paper", "scissor"]:
        print("Invalid choice, please enter rock, paper, or scissor.")
        continue 
    if user=="rock":
        if computer=="rock":
            print()
            print("User Enters : ",user)
            print("Computer Enters : ",computer)
            print("Draw")
            print()
        elif computer=="scissors":
            print()
            print("User Enters : ",user)
            print("Computer Enters : ",computer)
            print("User Wins")
            print()
        else:
            print()
            print("User Enters : ",user)
            print("Computer Enters : ",computer)
            print("Computer Wins")
            print()
    elif user=="paper":
        if computer=="paper":
            print()
            print("User Enters : ",user)
            print("Computer Enters : ",computer)
            print("Draw")
            print()
        elif computer=="rock":
            print()
            print("User Enters : ",user)
            print("Computer Enters : ",computer)
            print("User Wins")
            print()
        else:
            print()
            print("User Enters : ",user)
            print("Computer Enters : ",computer)
            print("Computer Wins")
            print()    
    else:
        if computer=="scissors":
            print()
            print("User Enters : ",user)
            print("Computer Enters : ",computer)
            print("Draw")
            print()
        elif computer=="paper":
            print()
            print("User Enters : ",user)
            print("Computer Enters : ",computer)
            print("User Wins")
            print()
        else:
            print()
            print("User Enters : ",user)
            print("Computer Enters : ",computer)
            print("Computer Wins")
            print()
    Game=input("Enter any key to continue OR Enter exit to Stop the Game : ")
    print()
print("Thank you")