print("I'm going to guess how old are you.")
choice = 0
answer = "n"

while answer == "n":
    choice = choice + 1
    answer = input("Are you " + str(choice) + "? (y/n): ")  # ← Fixed this line
print("I knew you were " + str(choice) + " years old.")