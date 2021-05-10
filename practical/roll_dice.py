import random

dice_limit = int(input("How many sides to the di? "))
roll = random.randint(1, (dice_limit))
guess = int(input("Guess the dice roll: \n"))

def fair_guess(active_guess):
    for num in range(1, (dice_limit + 1)):
        if num == active_guess:
            return True
    return False

def translate(num):
    translator = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six"
    }
    if num <= 6:
        return translator[num]
    else:
        return num

if not fair_guess(guess):
    print(f"Please guess a number between 1 and {dice_limit} next time.")
elif guess == roll:
    print(f"Wow! you guessed right it was {translate(roll)}!")
else:
    print(f"Oh sorry your guess of {translate(guess)} was wrong, it was {translate(roll)}.")