from random import choice

human_won = choice(["Blind squirrel found a nut", "Computer lost to dumb human",
        "Enjoy it while you can", "Dumb human got lucky"])

comp_won = choice(["Computer beats the dipshit human.", "Computer wins, hahaha.",
        "Inferior human loses again.", "How are you going to win a simple game if you can't keep ass hats out of the oval office?"])

human = input("Make your selection: [r]ock, [p]aper, or [s]cissors\n> ")

if human == "r" or human == "rock":
    human = "rock"

elif human == "s" or human == "scissors":
    human = "scissors"

elif human == "p" or human == "paper":
    human = "paper"

else:
    print("Make a valid selection, dumbass!")

computer = choice(["rock", "paper", "scissors"])
print(f"Computer's choice is {computer}.\n")

if computer == human:
    print("Tie game. Shoot again.")

elif computer == "scissors" and human == "paper":
    print(f"{computer} cuts {human}. {comp_won}")

elif computer == "paper" and human == "rock":
    print(f"{computer} covers {human}. {comp_won}")

elif computer == "rock" and human == "scissors":
    print(f"{computer} smashes {human}. {comp_won}")

elif human == "scissors" and computer == "paper":
    print(f"{human} cuts {computer}. {human_won}.")

elif human == "paper" and computer == "rock":
    print(f"{human} covers {computer}. {human_won}.")

elif human == "rock" and computer == "scissors":
    print(f"{human} smashes {computer}. {human_won}.")

else:
    print("You suck at this game!")
