import random

dict = {1:"ROCK", 2:"PAPER", 3:"SCISSORS"}
kp = True

def Uchoice(): #function to take user input
    print("Enter your choice: \n1 for Rock \n2 for Paper \n3 for Scissors")
    ui = int(input())
    if ui == 1 or ui == 2 or ui == 3:
        return ui
    else:
        print("Please input appropiate choice: ")
        return Uchoice()
    

def Cchoice(): #Function to take random choice from computer
    ci = random.randint(1,3)
    return ci

def Compare(userChoice, randomChoice): #Function to compare values
    if userChoice == 1:
        if randomChoice == 2:
            print(dict[1], "vs", dict[2], "\nYou Lose") #Rock vs Paper
        if randomChoice == 3:
            print(dict[1], "vs", dict[3], "\nYou Win" ) #Rock vs Scissors  
            
    if userChoice == 2:
        if randomChoice == 1:
            print(dict[2], "vs", dict[1], "\nYou Win" ) #Paper vs Rock
        if randomChoice == 3:
            print(dict[2], "vs", dict[3], "\nYou Lose") #Paper vs Scissors           
            
    if userChoice == 3:
        if randomChoice == 1:
            print(dict[3], "vs", dict[1], "\nYou Lose") #Scissors vs Rock
        if randomChoice == 2:
            print(dict[3], "vs", dict[2], "\nYou Win" ) #Scissors vs Paper
            
    if userChoice == randomChoice:
        print(dict[userChoice], "vs", dict[randomChoice], "\nDraw")
        #INSTANT REGAME AFTER DRAW
            
            
def playagain(): #Function to allow user to decide to continue playing or not
    ask = input().strip().upper()
    if ask.startswith("Y"):
        kp = True
        return kp
    elif ask.startswith("N"):
        kp = False
        return kp
    else:
        print("PLease put yes or no")
        return playagain()

#main
print("Welcome to Rock Paper Scissors Game")
while kp:
    uc = Uchoice()
    rc = Cchoice()
    Compare(uc, rc)
    print("Do you want to play again: Yes or No ")
    kp = playagain()

    
    
    




