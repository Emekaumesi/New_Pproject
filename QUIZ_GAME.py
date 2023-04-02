print ("WELCOME TO MY GAME, MO'FUCKERS")

question = input ("Do you want to play my game? ")
if question.lower() == "yes":
    print ("Now you are ready!")
else:
    quit()
score = 0

answer = input("What is the meaning of CR7? ")
if answer.lower() == "cristiano ronaldo":
    print("Correct Guy! Make we continue")
    score += 1
else:
    print("You no sabi football, make we sha dey go? ")

answer = input("Who is the greatest player in the world right now? ")
if answer.lower() == "cristiano ronaldo" or "messi":
    print("Correct Guy! Make we continue")
    score += 1
else:
    print("You no sabi football, make we sha dey go? ")

answer = input("What is the coach of Man city? ")
if answer.lower() == "Pep" or "Guardiola" or "Pep Guardiola":
    print("Correct Guy! Make we continue")
    score += 1
else:
    print("You no sabi football, make we sha dey go? ")

answer = input("Who is the highest goal scorer in the EPL this season? ")
if answer.lower() == "Haaland" or "Erling" or "Erling Haaland":
    print("Correct Guy! Make we continue")
    score += 1
else:
    print("You no sabi football, make we sha dey go? ")

print (f"You got {score} questions correctly")
print (f"You got {score/4 * 100}% questions correctly")