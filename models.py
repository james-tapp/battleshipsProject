from methods import buildBoardShips

directions = ["u","d","l","r"]

inputs = ["1","2","3","4","5","6","7","8","9","0"]

cheat = False


class Player:
    def __init__(self, playerNumber):
        self.playerNumber = playerNumber
        self.shipsBoard = buildBoardShips(boardLength)
        self.shotsBoard = buildBoardShips(boardLength, False)
        self.alive = True
        self.hitsLeft = 2*int(destroyerNumber) + 3*int(cruiserNumber) + 3*int(submarineNumber) + 4*int(battleshipNumber) + 5*int(carrierNumber)


class Destroyer:
    def __init__(self, destroyerNum):
        self.length = 2
        self.number = destroyerNum
        self.name = "destroyer"

class Cruiser:
    def __init__(self, cruiserNum):
        self.length = 3
        self.number = cruiserNum
        self.name = "cruiser"

class Submarine:
    def __init__(self, submarineNum):
        self.length = 3
        self.number = submarineNum
        self.name = "submarine"

class Battleship:
    def __init__(self, battleshipNum):
        self.length = 4
        self.number = battleshipNum
        self.name = "battleship"

class Carrier:
    def __init__(self, carrierNum):
        self.length = 5
        self.number = carrierNum
        self.name = "carrier"

        
        



