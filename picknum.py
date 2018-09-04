from random import randint
keep_going = "y"
upper_limit = 100
counter = 0
randy = randint(1, upper_limit)
user = None

while randy != user:
    counter += 1
    user = int(input(f"Pick a number from 1 to {upper_limit}\n"))
    if user > randy:
        print("Too high")

    elif user < randy:
        print("Too low")

    else:
        print("You got it!")

if counter == 1:
    print("It took you one guess to get it right.")

else:
    print(f"It took you {counter} guesses to get the right answer.")
