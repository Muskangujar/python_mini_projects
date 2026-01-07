import random

user_wins = 0
computer_wins = 0
options = ["r","p","s"]

while True:
    user_input= input("Type R/P/S or Q to Quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        print("Don't Act Oversmart Put A Proper Value")
        continue

    random_number = random.randint(0,2)
    
    # 0 = R, 1 = P, 1 = S
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "r" and computer_pick == "s":
        print("Damn! You Won")
        user_wins += 1
        continue
    elif user_input == "p" and computer_pick == "r":
        print("Damn! You Won")
        user_wins += 1
    elif user_input == "s" and computer_pick == "p":
        print("Damn! You Won")
        user_wins += 1
    else: 
        print("You Lost!")
        computer_wins += 1

print("You won", user_wins,"times")
print("Computer won",computer_wins,"times")

if computer_wins > user_wins:
    print("Looser")
elif computer_wins == user_wins:
    print("Hmm")
else:
    print("You are Goodddd")
    
print("Bye! :(")