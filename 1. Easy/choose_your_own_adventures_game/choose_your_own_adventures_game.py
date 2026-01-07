name  = input("type your name:")
print("Welcome",name,"to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()
if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross? Type Walk or Swim").lower()
    if answer == "swim":
        print("Opsie there was an crocodile,You lose")
    elif answer == "walk" :
        print("Yay you are now queen of the castle as you look like the lost princess")
    else:
        print("Not a valid option you lose")
elif answer == "right":
    print("You have reached the Island and Yay you are now queen of the castle as you look like the lost princess")
else:
    print("Not a correct option you lose")