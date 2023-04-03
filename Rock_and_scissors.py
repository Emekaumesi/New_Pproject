import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quite: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    #0 represents rock, 1 stands for paper, 2 stands for scissors
    computer_pick = options [random_number]
    print(f"The computer picked {computer_pick}")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
        continue
    else:
        print("You lost! The computer won!")
        computer_wins += 1

print(f"You won {user_wins} times")
print(f"The Computer won {computer_wins} times")



print("Goodby, bro!")


