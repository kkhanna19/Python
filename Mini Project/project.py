import random

target = random.randint(1, 100)

while True:
    userChoice = input("Guess the target or Quit : ")
    if(userChoice == "q"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success")
        break
    elif(userChoice < target):
        print("Small Number")
    else:
        print("Too Large")
    
print("-----Game Over-----")
