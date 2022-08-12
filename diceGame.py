# Viola Dube
# Dice Game - up and down the mountain

import random

# initialize  global variables
playerStep = 0
compStep = 0
winner = False
playerReachedTop = False
compReachedTop = False


# functions defined

#Roll the die
def RollDie():
    rolledDie = random.randint(1,6)
    return rolledDie


#Display rolled die in numeric and picture form to user
def DisplayDieRoll(number):
    print("Die roll result is a ", number, "\n")
    if number == 1 :
        print("-----" )
        print("|   |" )
        print("| . |" )
        print("|   |")
        print("-----")
    elif number == 2:
        print("-----" )
        print("|.  |" )
        print("|   |" )
        print("|  .|")
        print("-----")       
    elif number == 3:
        print("-----" )
        print("|.  |" )
        print("| . |" )
        print("|  .|")
        print("-----")              
    elif number == 4:
        print("-----" )
        print("|. .|" )
        print("|   |" )
        print("|. .|")
        print("-----")              
    elif number == 5:
        print("-----" )
        print("|. .|" )
        print("| . |" )
        print("|. .|")
        print("-----")              
    elif number == 6:
        print("-----" )
        print("|. .|" )
        print("|. .|" )
        print("|. .|")
        print("-----")              
    else:
        print("Invalid die roll")


# Check if player or computer gets to move to the next step
# If able to advance to next step, update step value
def CheckAdvanceNextStep(roll, who):
    global playerStep
    global compStep
    global playerReachedTop
    global compReachedTop

    
    if who == "player":
        # figure out next possible step for player
        if playerReachedTop:
            nextStep = playerStep - 1
        else:
            nextStep = playerStep + 1

        # if the roll equals the next step than player advances to next step
        if roll == nextStep:
            playerStep = nextStep
            if playerStep == 6:
                playerReachedTop = True
        
    else:  # who is the computer
         # figure out next possible step for computer
        if compReachedTop:
            nextStep = compStep - 1
        else:
            nextStep = compStep + 1

        # if the roll equals the next step than player advances to next step
        if roll == nextStep:
            compStep = nextStep
            if compStep == 6:
                compReachedTop = True       
    
    




# Display info about game to user
def DisplayResults():
    print("Player is on step ", playerStep, "Computer is on step ", compStep, "\n")


#check if player or computer has won the game
def CheckForWinner():
    winner = False
    if playerStep == 1 and playerReachedTop and compStep == 1 and compReachedTop:
        winner = True
        print("It is a tie!  Player and computer are both winners.")    
    elif playerStep == 1 and playerReachedTop:
        winner = True
        print("The player has won the game!")
    elif compStep == 1 and compReachedTop:
        winner = True
        print("The computer has won the game!")
    else:
        winner = False
        
    return winner


# main program
print("In this dice game you will take turns against the computer rolling a die to climb up and down the mountain.")
print("The object of this game is to get the numbers 1 up to 6 in order and then back down to 1 in order.")
print("Six is the top of the mountain and you must get a 1 to start your climb.")
print("Will you or the computer finish the hike up and down the mountain first?")

while winner == False:
    print("Player's turn")
    ready = input("Hit any key to roll the dice")
    playerRoll = RollDie()
    DisplayDieRoll(playerRoll)
    CheckAdvanceNextStep(playerRoll, "player")
    
    print("Computer's turn")
    ready = input("Hit any key to roll the dice")
    compRoll = RollDie()
    DisplayDieRoll(compRoll)
    CheckAdvanceNextStep(compRoll, "computer")
    
    DisplayResults()
    winner = CheckForWinner()

print("Game over. Thanks for playing.")

