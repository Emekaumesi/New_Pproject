import random

top_of_range = input ("Type a number ")
if top_of_range.isdigit:
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time")
        quit()
else:
    print("Type a number next time!")
    quit()
random_number = random.randint(0, top_of_range)

number_of_guesses = 0

while True:
    number_of_guesses += 1
    user_guess = input ("Make a wild number guess ")
    if user_guess.isdigit:
        user_guess = int(user_guess)
    else:
        print("Next time, be smart and type a number instead")
        continue
    if user_guess == random_number:
        print("Your guessing Game is A+")
        break
    elif user_guess < random_number:
            print("Your guess was less than the number we want")
    else:
        print("It was more than the random number we want")

print(f"You guessed that {random_number} is the correct number. Big ups! But that was after you guessed {number_of_guesses} times")

