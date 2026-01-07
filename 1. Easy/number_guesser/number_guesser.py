import random

top_of_range = input("Type a Number : ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Print give a number grteater than 0")
        quit()
else:
    print("Please type a number and not a string")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a Guess!: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("type a number bitch")
        continue

    if user_guess == random_number:
        print("You got it correct my lorddd!")
        break
    elif user_guess > random_number:
        print("You are above the number")
    else:
        print("You are below the number")

print("Number of guesses = ", guesses ,"congratulations")