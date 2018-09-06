from random import randint
keep_going = "y"
upper_limit = input("Enter a number for the upper limit of the guessing game:\n> ")

if upper_limit.isdigit():
    upper_limit = int(upper_limit)

else:
    upper_limit = int(input("Yo! Enter digits!\n What is the upper limit?  "))

counter = 0
randy = randint(1, upper_limit)

cumulative_guesses = 0
game_count = 0

while True:
    counter += 1
    user = int(input(f"Pick a number from 1 to {upper_limit}\n"))
    if user > randy:
        print("Too high")

    elif user < randy:
        print("Too low")

    else:
        print("You got it!")
        cumulative_guesses += counter
        game_count += 1

        if counter == 1:
            print("It took you one guess to get it right.")
        else:
            print(f"It took you {counter} guesses to get it right.")

        play_again = input("Do you want to play again (y/n) ")
        if play_again == "y":

            randy = randint(1, upper_limit)

            counter = 0
        else:
            print("Thank you for playing, sucka.")
            ave_score = round((cumulative_guesses / game_count), 2)
            print(f"\n\nYour number of games played was {game_count}, \nand your average number of guesses per game was {ave_score}.")
            break
