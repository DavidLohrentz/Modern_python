from random import randint
keep_going = "y"
upper_limit = int(input("Enter a number for the upper limit of the guessing game:\n> "))
counter = 0
randy = randint(1, upper_limit)
user = None
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
            print(f"It took you {counter} guesses to get the right answer.")

        play_again = input("Do you want to play again (y/n) ")
        if play_again == "y":

            randy = randint(1, upper_limit)
            guess = None
            counter = 0
        else:
            print("Thank you for playing, sucka.")
            ave_score = float(cumulative_guesses) / game_count
            print(f"Your number of games played was {game_count}, and your average number of guesses was {ave_score}.")
            break
