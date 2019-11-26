

directions = ["u","d","l","r"]

inputs = ["1","2","3","4","5","6","7","8","9","0"]

cheat = False


def numericInput(string):
    string = str(string)
    valid = True
    if(string == ""):
        return(False)
    for i in range(0,len(string)):
        if(not(string[i] in inputs)):
            valid = False
            break
    return(valid)

def validDirection(u,v,board,length):

    directions = []

    x = int(u)

    y = int(v)

    l = 1

    if(x-1 + length <= len(board)):

        while(l<length and board[x+l-1][y]=="empty"):

            l=l+1

        if(l==length):

            directions.append("d")

        l = 1



    if(x-1 - length >= -1):

        while(l<length and board[x-l-1][y]=="empty"):

            l=l+1

        if(l==length):

            directions.append("u")



    l = 1

    if(y + length <= len(board)):

        while(l<length and board[x-1][y+l]=="empty"):

            l=l+1

        if(l==length):

            directions.append("r")



    l = 1

    if(y - length >= 0):

        while(l<length and board[x-1][y-l]=="empty" ):

            l=l+1

        if(l==length):

            directions.append("l")



    return directions


def placeShipsAi(obj, battleshipsList):

    tempBoard = obj.shipsBoard

    tempBattleships = [Destroyer(destroyerNumber), Submarine(submarineNumber), Cruiser(cruiserNumber), Battleship(battleshipNumber), Carrier(carrierNumber)]

    for i in range(5):
        while (int(tempBattleships[i].number)):
            
            x2 = random.randint(0,boardLength-1)
            y2 = random.randint(1,boardLength)

            while(tempBoard[x2][y2]!= "empty"):
                x2 = random.randint(0,boardLength-1)
                y2 = random.randint(1,boardLength)

            if (validDirection(x2+1, y2, tempBoard, tempBattleships[i].length)!= []):
                #place ships

                d2 = random.choice(validDirection(x2+1, y2, tempBoard, tempBattleships[i].length))

                

                if(d2 == "u"):
                    for j in range(tempBattleships[i].length):
                        tempBoard[x2-j][y2] = "ship"
                elif(d2 == "d"):
                    for j in range(tempBattleships[i].length):
                        tempBoard[x2+j][y2] = "ship"
                elif(d2 == "r" ):
                    for j in range(tempBattleships[i].length):
                        tempBoard[x2][y2+j] = "ship"
                elif(d2 == "l" ):
                    for j in range(tempBattleships[i].length):
                        tempBoard[x2][y2-j] = "ship"



                tempBattleships[i].number = (int(tempBattleships[i].number)-1) 


            else:
                print("failure!")
                return(False)
    return (tempBoard)

            
def placeShipsHuman(obj, battleshipsList):

    tempBoard = obj.shipsBoard
    tempBattleships = [Destroyer(destroyerNumber), Submarine(submarineNumber), Cruiser(cruiserNumber), Battleship(battleshipNumber), Carrier(carrierNumber)]

    #while (shipsLeft(tempBattleshipsList)):





    for i in range(5):
        while (int(tempBattleships[i].number) > 0):
            
            x1 = input(["which row would you like to place " + tempBattleships[i].name + " number " + (str(int(battleships[i].number)-int(tempBattleships[i].number)+1)) + " in? (length " + str(tempBattleships[i].length) + ")" ])

            y1 = input(["which column would you like to place " + tempBattleships[i].name + " number " + str(int(battleships[i].number)-int(tempBattleships[i].number)+1) + " in? (length " + str(tempBattleships[i].length) +")" ])
            
            while(not (numericInput(x1)) or not(numericInput(y1)) or int(x1)<1 or int(y1)<1 or int(x1)>boardLength or int(y1)>boardLength or tempBoard[int(x1)-1][int(y1)]!="empty" or int(x1)<1 or int(y1)<1 or int(x1)>boardLength or int(y1)>boardLength):
                if(numericInput(x1) and numericInput(y1)):
                    print("that square is not empty, please try again!")
                else:
                    print("invalid input, try again!")

                x1 = input(["which row would you like to place " + tempBattleships[i].name + " number " + (str(int(battleships[i].number)-int(tempBattleships[i].number)+1)) + " in? (length " + str(tempBattleships[i].length) + ")" ])

                y1 = input(["which column would you like to place " + tempBattleships[i].name + " number " + str(int(battleships[i].number)-int(tempBattleships[i].number)+1) + " in? (length " + str(tempBattleships[i].length) +")" ])

            x1 = int(x1)
            y1 = int(y1)

            if (validDirection(x1, y1, tempBoard, tempBattleships[i].length)!= []):
                #place ships

                d1 = input(["in which direction would you like this ship to travel? (u,d,l,r)"])

                while( not (d1 in validDirection(x1, y1, tempBoard, tempBattleships[i].length))):
                    print ("please enter a valid direction of travel")
                    d1 = input(["in which direction would you like this ship to travel? (u,d,l,r)"])

                    

                if(d1 == "u"):
                    for j in range(tempBattleships[i].length):
                        tempBoard[x1-j-1][y1] = "ship"
                elif(d1 == "d"):
                    for j in range(tempBattleships[i].length):
                        tempBoard[x1+j-1][y1] = "ship"
                elif(d1 == "r" ):
                    for j in range(tempBattleships[i].length):
                        tempBoard[x1-1][y1+j] = "ship"
                elif(d1 == "l" ):
                    for j in range(tempBattleships[i].length):
                        tempBoard[x1-1][y1-j] = "ship"                    
                    
                tempBattleships[i].number = (int(tempBattleships[i].number)-1) 


                for j in range(boardLength+1):
                    print(obj.shipsBoard[j])

            else:
                print("oops, something went wrong! try planning your ship placement more carefully")
                obj.shipsBoard = buildBoardShips(boardLength)
                tempBattleships = [Destroyer(destroyerNumber), Submarine(submarineNumber), Cruiser(cruiserNumber), Battleship(battleshipNumber), Carrier(carrierNumber)]
                return(False)

            

def fireShotsHuman():
    target = input(["which player would you like to target"])
    rowNumber = input(["which row would you like to target"])
    columnNumber = input(["which column would you like to target"])

    while( (not numericInput(target)) or (not numericInput(rowNumber)) or (not numericInput(columnNumber)) or (int(target) < 2) or (int(target) > playerNumber) or (int(columnNumber) < 1) or (int(columnNumber)>boardLength) or (int(rowNumber)> boardLength) or (int(rowNumber) < 1) or players[int(target)-1].shotsBoard[int(rowNumber)-1][int(columnNumber)] != "none" ):
        print("please try again")
        target = input(["which player would you like to target"])
        rowNumber = input(["which row would you like to target"])
        columnNumber = input(["which column would you like to target"])

    target = int(target) - 1
    rowNumber = int(rowNumber)-1
    columnNumber = int(columnNumber)
        
    if(players[target].shipsBoard[rowNumber][columnNumber] == "empty"):
        players[target].shotsBoard[rowNumber][columnNumber] = "miss"
        print("miss")

    elif(players[target].shipsBoard[rowNumber][columnNumber] == "ship"):
        players[target].shotsBoard[rowNumber][columnNumber] = "hit"
        players[target].hitsLeft -= 1
        print("hit")


        if(players[target].hitsLeft == 0):
            players[target].alive = False
            print("player number " + str(target) + " is now dead")


def fireShotsAi(AiNumber):
    target = random.randint(0,playerNumber-1)
    rowNumber = random.randint(0,boardLength-1)
    columnNumber = random.randint(1,boardLength)

    
    while(target == AiNumber or players[target].shotsBoard[rowNumber][columnNumber] != "none"):
        target = random.randint(0,playerNumber-1)
        rowNumber = random.randint(0,boardLength-1)
        columnNumber = random.randint(1,boardLength)

            
    if(players[target].shipsBoard[rowNumber][columnNumber] == "empty"):
        players[target].shotsBoard[rowNumber][columnNumber] = "miss"

    elif(players[target].shipsBoard[rowNumber][columnNumber] == "ship"):
        players[target].shotsBoard[rowNumber][columnNumber] = "hit"
        players[target].hitsLeft -= 1

        if(players[target].hitsLeft == 0):
            players[target].alive = False
        
        


#code to build a battleships board

def buildBoardShips(length,ships=True):
    board = []
    for i in range(1,length+1):
        board.append(["row " + str(i)])
    if(ships):        
        board.append(["BOARD"])
    else:
        board.append(["SHOTS"])
    for i in range(1, length+1):
        board[length].append("col " + str(i))
    for i in range(0, length):
        for j in range(length):
            if(ships):
                board[i].append("empty")
            else:
                board[i].append("none")

    return(board)


def aliveCount(Players):
    livingPlayers = 0
    for i in range(playerNumber):
        if (players[i].alive):
            livingPlayers += 1

    return(livingPlayers)
