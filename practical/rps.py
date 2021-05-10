import random
hands = ["rock", "paper", "scissors"]
their_hand = hands[random.randint(0,2)]
your_hand = input("rock, paper, or scissors? ")

if your_hand == their_hand:
    print ("tie game")
elif your_hand == "rock" and their_hand == "scissors":
    print ("You win, rock crushes scissors.")
elif your_hand == "paper" and their_hand == "rock":
    print ("You win, paper covers rock.")
elif your_hand == "scissors" and their_hand == "paper":
    print ("You win, scissors cut paper.")
else:
    print (f"computer drew a {their_hand}, You lost.")