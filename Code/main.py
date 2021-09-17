################################
################################
##      Projet - Démineur     ##
##       Version - 0.1        ##
## Touches Utiles - BGS / BDS ##
##         FougR              ##
##       17/09/2021           ##
################################
################################


from random import *

class Game_State():
    def __init__(self):
        self.userBoard = [[0, "-1", "-2", "-3", "-4", "-5"],
                        [1, "--", "--", "--", "--", "--"],
                        [2, "--", "--", "--", "--", "--"],
                        [3, "--", "--", "--", "--", "--"],
                        [4, "--", "--", "--", "--", "--"],
                        [5, "--", "--", "--", "--", "--"]]
        self.board = [["__", "__", "__", "__", "__", "__", "__"],
                        ["||", "--", "--", "--", "--", "--", "||"],
                        ["||", "--", "--", "--", "--", "--", "||"],
                        ["||", "--", "--", "--", "--", "--", "||"],
                        ["||", "--", "--", "--", "--", "--", "||"],
                        ["||", "--", "--", "--", "--", "--", "||"],
                        ["__", "__", "__", "__", "__", "__", "__"]]
        self.currentState = "Working"
        self.mines_restantes = 2
        self.DIMENSION = 5

    def minage(self):
        for i in range(3):
            x = randint(1,5)
            y = randint(1,5)
            print(x,y)
            if self.board[y][x] != "Bo":
                self.board[y][x] = "Bo"
            else:
                i = i - 1
        for r in range(1, self.DIMENSION + 1):
            for c in range(1, self.DIMENSION + 1):
                bombes_proches = 0
                if self.board[c][r] != "Bo":
                    for i in range(-1, 2):
                        if self.board[c+i][r-1] == "Bo":
                            bombes_proches = bombes_proches + 1
                        elif self.board[c+i][r] == "Bo":
                            bombes_proches = bombes_proches + 1
                        elif self.board[c+i][r+1] == "Bo":
                            bombes_proches = bombes_proches + 1
                        self.board[c][r] = "-" + str(bombes_proches)

    def drapeau(self, x, y):
        self.userBoard[y][x] = "Dr"

    def creuser(self, x, y):
        bombes_proches = 0
        if self.board[y][x] == "Bo":
            self.currentState = "Loose"
        else:
            self.userBoard[y][x] = self.board[y][x]
##            val = self.board[y][x]
##            self.userBoard[y][x] = val

    def gagner(self):
        caseAcreuser = 0
        for r in range(1, self.DIMENSION):
            for c in range(1, self.DIMENSION):
                if self.userBoard[c][r] == "--":
                    caseAcreuser = caseAcreuser + 1
        if caseAcreuser == 0:
            self.currentState = "Win"


def main():
    Game = Game_State()
    Game.minage()
    for i in range(len(Game.board)):
        print(Game.board[i])
    while Game.currentState == "Working":
        action = input("Creuser (c) ou planter un Drapeau (d) ?")
        if action == "c":
            x = int(input("x ?"))
            y = int(input("y ?"))
            Game.creuser(x,y)
            for i in range(len(Game.userBoard)):
                print(Game.userBoard[i])
        elif action == "d":
            x = int(input("x ?"))
            y = int(input("y ?"))
            Game.drapeau(x,y)
            for i in range(len(Game.userBoard)):
                print(Game.userBoard[i])
        Game.gagner()

    if Game.currentState == "Win":
        print("You Win !")
    elif Game.currentState == "Loose":
        print("You Blew Up on a landmine...")

main()
