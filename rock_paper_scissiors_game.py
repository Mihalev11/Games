from random import randint

player_name = input("Hello, what's your name?")

print("Okay, " + player_name+ " Let's play Rock, Papper, Scissiors" )
#create a list of play options
t = ["Rock", "Papper", "Scissiors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
    player = input("Rock, Papper, Scissiors")
    if player == computer:
        print("Tie!")
    elif player == ("Rock"):
        if computer == ("Papper"):
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == ("Papper"):
        if computer == ("Scissiors"):
            print("You lose", computer, "cut", player)
        else:
            print("You win", player, "covers", computer)
    elif player == ("Scissiors"):
        if computer == ("Rock"):
            print("You lose", computer, "smashed", player)
        else:
            print("You win", player, "cut", computer)
    else:
        print("That's not a valid play! Check your spelling!")
#player was set to True, but we want it to be False to the loop continues
    player = False
    computer=t[randint(0,2)]






