from random import randint

searched = randint(1, 100)
number_of_guesses = 0
while True:
    try:
        guess = (input("Guess the number: "))
        guess = int(guess)
        if 0 < guess <= 100:
            number_of_guesses += 1
            if searched > guess:
                print("Too low!")
            elif searched < guess:
                print("Too high!")
            else:
                print(f"You won! It took you {number_of_guesses} guesses!")
                break
        else:
            print("Pick a number between 1 and 100")
    except ValueError:
        print(f"{guess} is not a natural number!")
