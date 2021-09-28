################################
################################
##      Projet - Démineur     ##
##       Version - 0.1        ##
## Touches Utiles - BGS / BDS ##
##         FougR              ##
##       17/09/2021           ##
################################
################################


#Importation Librairie
from random import *
from pygame import *

#Variable pour l'interface graphique
WIDTH = HEIGHT = 512
DIMENSION = 5
SQ_SIZE = HEIGHT // DIMENSION
IMAGES = {}

class Game_State():

    #Toutes les coordonnées des cases sont inversées, ce sera y,x au lieu de x,y

    def __init__(self):
        self.userBoard = [["00", "-1", "-2", "-3", "-4", "-5", "__"],
                        ["01", "--", "--", "--", "--", "--", "||"],
                        ["02", "--", "--", "--", "--", "--", "||"],
                        ["03", "--", "--", "--", "--", "--", "||"],
                        ["04", "--", "--", "--", "--", "--", "||"],
                        ["05", "--", "--", "--", "--", "--", "||"],
                        ["_", "__", "__", "__", "__", "__", "__"]]
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
            x = randint(1,5) #coordonnées aléaroires des bombes
            y = randint(1,5)
            print(x,y)
            if self.board[y][x] != "Bo": #Les bombes sont mises à l'emplacement des coordonnées aléatoires définies au dessus
                self.board[y][x] = "Bo"
            else:
                i = i - 1
        for r in range(1, self.DIMENSION + 1): #Détection case par case du nombre de bombes dans les 8 cases adjacentes
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
                        self.board[c][r] = "-" + str(bombes_proches) #Numérotation des cases de la grilles de jeu

    #Plante un drapeau
    def drapeau(self, x, y):
        self.userBoard[y][x] = "Dr"

    #Creuse une case
    def creuser(self, x, y):
        bombes_proches = 0
        if self.board[y][x] == "Bo": #Détection bombes déclenchées
            self.currentState = "Loose"
        else:
            self.userBoard[y][x] = self.board[y][x] #Révélation numéro de la case creusée
##            val = self.board[y][x]
##            self.userBoard[y][x] = val
            for y in range(1, self.DIMENSION):  #Si numéro case = 0 alors afficher toutes les cases autour (Il faut une boucle récursive pour le faire, pour l'instant seulement les 8 cases adjacente sont affichées
                for x in range(1, self.DIMENSION):
                    if self.userBoard[y][x] == "-0":
                        print("Coucou")
                        for i in range(-1, 2):
                            self.userBoard[y+i][x-1] = self.board[y+i][x-1]
                            self.userBoard[y+i][x] = self.board[y+i][x]
                            self.userBoard[y+i][x+1] = self.board[y+i][x+1]
##            if self.board[y][x] == "-0":
##                for i in range(-1, 2):
##                    self.userBoard[y+i][x-1] = self.board[y+i][x-1]
##                    print("1/3/", i)
##                    self.userBoard[y+i][x] = self.board[y+i][x]
##                    print("2/3/", i)
##                    self.userBoard[y+i][x+1] = self.board[y+i][x+1]
##                    print("3/3/", i)
##                    #for i in range(len(self.userBoard)):
##                        #print(self.userBoard[i])

    #Détection Victoire
    def gagner(self):
        caseAcreuser = 0
        for r in range(1, self.DIMENSION):
            for c in range(1, self.DIMENSION):
                if self.userBoard[c][r] == "--":
                    caseAcreuser = caseAcreuser + 1
        if caseAcreuser == 0:
            self.currentState = "Win"


##def loadImages():
##    pieces = ["--", "-0", "-1", "-2", "-3", "Bo", "Dr"]
##    for i in pieces:
##        IMAGES[piece] = pygame.image.load("Assets/" + pieces + ".png")
##
##def main():
##    pygame.init()
##    screen = pygame.display.set_mode((WIDTH,HEIGHT))
##    screen.fill(pygame.Color("white"))
##    loadImages()
##    gs = Game_State()


def main():
    Game = Game_State() #création objet démineur
    Game.minage() #Placement des bombes
    for i in range(len(Game.board)): #Permet d'afficher le jeu sur la console
        print(Game.board[i])
    while Game.currentState == "Working": #COndition d'arret du jeu : self.currentState == "Loose"
        action = input("Creuser (c) ou planter un Drapeau (d) ?")
        if action == "c": #action creuser
            x = int(input("x ?"))
            y = int(input("y ?"))
            Game.creuser(x,y)
            for i in range(len(Game.userBoard)):
                print(Game.userBoard[i])
        elif action == "d": #action planter un drapeau
            x = int(input("x ?"))
            y = int(input("y ?"))
            Game.drapeau(x,y)
            for i in range(len(Game.userBoard)): #affiche la grille de jeu
                print(Game.userBoard[i])
        Game.gagner() #détection victoire

    if Game.currentState == "Win": #Détection Victoire
        print("You Win !")
    elif Game.currentState == "Loose": #Détection Défaite
        print("You Blew Up on a landmine...")

main()
