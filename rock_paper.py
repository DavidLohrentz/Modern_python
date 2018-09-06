from random import choice

match_length = input("How many games wins the match? \n> ")
if match_length.isdigit():
    match_length = int(match_length)

else:
    match_length = int(input("Yo! Dumbass! \nEnter a digit! How many games wins the match?? "))
player_wins = 0
computer_wins = 0

while player_wins < match_length and computer_wins < match_length:
    human_won = choice(["Blind squirrel found a nut", "Computer lost to dumb human",
            "Enjoy it while you can", "Dumb human got lucky"])

    comp_won = choice(["Computer beats the dipshit human.", "Computer wins, hahaha.",
            "Inferior human loses again.", "Sausages, Sausages. Barely even human!"])

    human = input("Make your selection: [r]ock, [p]aper, or [s]cissors\n> ").lower()

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
        print(f"{computer.capitalize()} cuts {human}. {comp_won}")
        computer_wins += 1
        print(f"Human: {player_wins}, Computer: {computer_wins}")

    elif computer == "paper" and human == "rock":
        print(f"{computer.capitalize()} covers {human}. {comp_won}")
        computer_wins += 1
        print(f"Human: {player_wins}, Computer: {computer_wins}")

    elif computer == "rock" and human == "scissors":
        print(f"{computer.capitalize()} smashes {human}. {comp_won}")
        computer_wins += 1
        print(f"Human: {player_wins}, Computer: {computer_wins}")

    elif human == "scissors" and computer == "paper":
        print(f"{human.capitalize()} cuts {computer}. {human_won}.")
        player_wins += 1
        print(f"Human: {player_wins}, Computer: {computer_wins}")

    elif human == "paper" and computer == "rock":
        print(f"{human.capitalize()} covers {computer}. {human_won}.")
        player_wins += 1
        print(f"Human: {player_wins}, Computer: {computer_wins}")

    elif human == "rock" and computer == "scissors":
        print(f"{human.capitalize()} smashes {computer}. {human_won}.")
        player_wins += 1
        print(f"Human: {player_wins}, Computer: {computer_wins}")

    else:
        print("You suck at this game!")

if player_wins > computer_wins:
    print("Human wins the match.\n\n" * 100000)

else:
    print("Computer wins the match.")
