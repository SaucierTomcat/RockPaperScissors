import random
print("""Hey, do you wanna play rock, paper, scissors? The rules are simple: 
Pick either rock, paper or scissors - rock beats scissors, scissors beats paper and paper beats rock.
The computer will pick another at random and depending on what you pick you win, lose or tie.""")
choices = ["rock", "paper", "scissors"]
while True:
    user = input("Go ahead and pick: rock, paper or scissors? ")
    npc = random.choice(choices)
    print("you picked:", user)
    print("computer picked:", npc)
    if user == "rock":
        if npc == "rock":
            print("Its a draw!")
        elif npc == "paper":
            print("Oh sorry, you lose!")
        elif npc == "scissors":
            print("Hey, you win!!!")
    elif user == "paper":
        if npc == "rock":
            print("Hey, you win!")
        elif npc == "paper":
            print("Its a draw!")
        elif npc == "scissors":
            print("Oh sorry, you lose!")
    elif user == "scissors":
        if npc == "rock":
            print("Oh sorry, you lose!")
        elif npc == "paper":
            print("Hey, you win!")
        elif npc == "scissors":
            print("Its a draw")
    else:
        print("none of those are the options we said, wth")
    x = input("Enter 0 to quit or anything else to play again ")
    if x == "0":
        break
    
