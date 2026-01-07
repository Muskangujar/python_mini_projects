print("Welcome to My game")

playing = input("Do you want to play? ")

if playing.lower() != "yes" : #TRUE
    quit()
print("Okay! Lets Play")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit" :
    print("Hurray Correct! :) ")
    score += 1
else:
    print("Oopsiee Try Again :( ")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit" :
    print("Hurray Correct! :) ")
    score += 1
else:
    print("Oopsiee Try Again :( ")

answer = input("What does ASAP stand for? ")
if answer.lower() == "as soon as possible" :
    print("Hurray Correct! :) ")
    score += 1
else:
    print("Oopsiee Try Again :( ")

answer = input("What does u&m stand for? ")
if answer.lower() == "you and me" :
    print("Hurray Correct! :) ")
    score += 1
else:
    print("Oopsiee Try Again :( ")

print("Congrats you scored!! ;): "+ str((score/4) * 100) + "You got " + str(score) + " questions correct")