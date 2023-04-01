


# name = input("what is your name? ")
names = []
with open("names.txt") as file:
  #read lines has a special function, readlines(), developed in the f/io documentation
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, key=str.lower):
    print(name)