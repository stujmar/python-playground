import random

roll = random.randint(1,6)
guess = int(input("Guess the dice roll: \n"))

def fair_guess(active_guess):
    for num in range(1,7):
        if num == active_guess:
            return True
    return False

translator = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six"
}

if not fair_guess(guess):
    print("Please guess a number between 1 and 6 next time.")
elif guess == roll:
    print(f"Wow! you guessed right it was {translator[roll]}")
else:
    print(f"Oh sorry your guess of {translator[guess]} was wrong, it was {translator[roll]}.")