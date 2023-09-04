import random

# init/declare
exit = False
userPoints = 0
computerPoints = 0

# start loop
while exit == False: # game ended when exit value = True
    options = ["rock", "paper", "scissors"]
    userInput = input("Chooser rock, paper, or scissors (or exit): ")
    computerInput = random.choice(options)

    # user input exit
    if userInput == "exit":
        print("Game ended")
        print("You won a total score of "+str(userPoints)+" and the enemy total score is "+str(computerPoints))
        exit = True

    # user input rock
    elif userInput == "rock":
        if computerInput == "rock":
            print("Your input is rock")
            print("Enemy input is rock")
            print("It is a tie (rock)!")
        elif computerInput == "paper":
            print("Your input is rock")
            print("Enemy input is paper")
            print("Enemy wins!")
            computerPoints += 1
        elif computerInput == "scissors":
            print("Your input is rock")
            print("Enemy input is scissors")
            print("You win!")
            userPoints += 1

    # user input paper
    elif userInput == "paper":
        if computerInput == "paper":
            print("Your input is paper")
            print("Enemy input is paper")
            print("It is a tie (paper)!")
        elif computerInput == "scissors":
            print("Your input is paper")
            print("Enemy input is scissors")
            print("Enemy wins!")
            computerPoints += 1
        elif computerInput == "rock":
            print("Your input is paper")
            print("Enemy input is rock")
            print("You win!")
            userPoints += 1
    
    # user input paper
    elif userInput == "scissors":
        if computerInput == "scissors":
            print("Your input is scissors")
            print("Enemy input is scissors")
            print("It is a tie (scissors)!")
        elif computerInput == "rock":
            print("Your input is scissors")
            print("Enemy input is rock")
            print("Enemy wins!")
            computerPoints += 1
        elif computerInput == "paper":
            print("Your input is scissors")
            print("Enemy input is paper")
            print("You win!")
            userPoints += 1

    # user input invalid string/input
    elif userInput != "rock" or userInput != "paper" or userInput != "scissors":
        print("Invalid input!")