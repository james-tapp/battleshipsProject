from methods import *

from models import *

import random

                
start = False
shipLimit = False

while(not start):
    boardLength = input(["What size board would you like to play with?"])

    if(boardLength == "cheat"):
        print("cheats enabled! well done for finding this ;)")
        cheat = True

    while( (not numericInput(boardLength) ) or ( int(boardLength)< 3)):

        print("invalid entry, try again!")

        boardLength = input(["What size board would you like to play with?"])

    boardLength = int(boardLength)

    if(boardLength < 6):
        print("choose a bigger board to unlock more ships!")

    playerNumber = input(["How many players would you like in this game?"])
        
    while( not (numericInput(playerNumber)) or int(playerNumber)<2 ):
        
        print ("invalid entry, try again!")

        playerNumber = input(["How many players would you like in this game?"])
        

    destroyerNumber = input(["How many destroyers would you like in this game? (length 2)"])

    if(boardLength > 3):

        submarineNumber = input(["How many submarines would you like in this game? (length 3)"])

    else:
        submarineNumber = 0

    if(boardLength > 4):

        cruiserNumber = input(["How many cruisers would you like in this game? (length 3)"])

    else:
        cruiserNumber = 0

    if(boardLength > 5):

        battleshipNumber = input(["How many battleships would you like in this game? (length 4)"])

    else:
        battleshipNumber = 0

    if(boardLength > 6):

        carrierNumber = input(["How many carriers would you like in this game? (length 5)"])

    else:
        carrierNumber = 0
    
    while((not numericInput(destroyerNumber) or  not numericInput(submarineNumber) or not numericInput(cruiserNumber) or not numericInput(battleshipNumber) or not numericInput(carrierNumber)) or pow(int(boardLength), 2) <= int(destroyerNumber)*2 + int(submarineNumber)*3 + int(cruiserNumber)*3 + int(battleshipNumber)*4 + int(carrierNumber)*5):


        print("invalid entry, try again")

        print("the total length of all ships must be less than " + str(pow(int(boardLength),2)))

        print("please enter a number 0 or greater for each ship type")

        destroyerNumber = input(["How many destroyers would you like in this game? (length 2)"])

        if(boardLength > 3):

            submarineNumber = input(["How many submarines would you like in this game? (length 3)"])

        else:
            submarineNumber = 0

        if(boardLength > 4):

            cruiserNumber = input(["How many cruisers would you like in this game? (length 3)"])

        else:
            cruiserNumber = 0

        if(boardLength > 5):

            battleshipNumber = input(["How many battleships would you like in this game? (length 4)"])

        else:
            battleshipNumber = 0

        if(boardLength > 6):

            carrierNumber = input(["How many carriers would you like in this game? (length 5)"])

        else:
            carrierNumber = 0

        

        
        

    if(int(playerNumber) > 4 or int(boardLength) > 13):

        confirm = input(["This game exceeds the recommended settings, would you like to continue (y/n)"])

        if(confirm == "y"):

            start = True

    else:

        start = True

boardLength = int(boardLength)
playerNumber = int(playerNumber)
battleships = [Destroyer(destroyerNumber), Submarine(submarineNumber), Cruiser(cruiserNumber), Battleship(battleshipNumber), Carrier(carrierNumber)]


players = []

for i in range(0, playerNumber):
    players.append(Player(i))


tempBoard = players[0].shipsBoard


#place ships on board
for i in range(0, boardLength+1):        
    print(players[0].shipsBoard[i])

while ( placeShipsHuman(players[0],battleships) == False):
    print("please try again")



for i in range(1,playerNumber):
    while (placeShipsAi(players[i], battleships) == False):
        print("oh no we have to try again")




if (cheat):
    for i in range(1, playerNumber):
        print("player number " + str(i+1))
        for j in range(boardLength+1):
            print(players[i].shipsBoard[j])
            



            

while(aliveCount(players) > 1):
    if(players[0].alive):
        fireShotsHuman()

    for i in range(1,playerNumber):
        if(players[i].alive):
            fireShotsAi(i)

    for i in range(playerNumber):
        if(i==0):
            print("human player")
        else:
            print("player " + str(i+1))
        for j in range(boardLength+1):
            print(players[i].shotsBoard[j])

if(players[0].alive):
    print("woohoo! you won")

else:
    print("you lose, better luck next time")

    
    


    


