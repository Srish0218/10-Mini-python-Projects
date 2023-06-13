print("Welcome to my python quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What will be the output of the following code snippet?\n print(2**3 + (5 + 6)**(1 + 1)) ")
if answer.lower() == "129":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("How is a code block indicated in Python? ")
if answer.lower() == "indentation":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Which types of loops are not supported in Python? ")
if answer.lower() == "do-while":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What keyword is used in Python to raise exceptions? ")
if answer.lower() == "raise":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions out os 4 questions correct!")
print("You got " + str((score / 4) * 100) + "%.")