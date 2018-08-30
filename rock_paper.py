from random import choice
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
    print(f"{computer} cuts {human}. Computer wins, sucka.")

elif computer == "paper" and human == "rock":
    print(f"{computer} covers {human}. Computer beats the dumb human.")

elif computer == "rock" and human == "scissors":
    print(f"{computer} smashes {human}. Computer wins.")

elif human == "scissors" and computer == "paper":
    print(f"{human} cuts {computer}. Human got lucky.")

elif human == "paper" and computer == "rock":
    print(f"{human} covers {computer}. Stupid Human somehow wins.")

elif human == "rock" and computer == "scissors":
    print(f"{human} smashes {computer}. Human wins.")

else:
    print("You suck at this game!")
