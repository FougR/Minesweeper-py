                ####################################
                ####################################
                ##        Projet - Démineur       ##
                ##          Version - 5           ##
                ##      Fichier - Librairie       ##
                ##  Nom Librairie - minesweeeper  ##
                ##   Touches Utiles - BGS / BDS   ##
                ##         Luc-Alexandre          ##
                ##           17/10/2021           ##
                ####################################
                ####################################



# Importation librairie
import random
import pygame as p
from tkinter import *
from tkinter import messagebox

# Création variable globale
#WIDTH = HEIGHT = ""
DIMENSION = ""
SQ_SIZE = ""
IMAGES = {}

Tk().wm_withdraw() # setup tkinter

# Création de l'objet Board pour représenter le démineur
class Board():
    def __init__(self, dim_size, num_bombs):
        # on garde des traces de ses valeurs, elle nous seront utiles plus tard
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # génération de deux nouveau board
        self.board = [['--' for _ in range(self.dim_size)] for _ in range(self.dim_size)] # grille de jeu prérempli par l'ordinateur
        self.visible_board = [['--' for _ in range(self.dim_size)] for _ in range(self.dim_size)] # grille de jeu affiché à l'écran
        # ceci créer un array comme ceci:
        # [[None, None, ..., None],
        #  [None, None, ..., None],
        #  [...                  ],
        #  [None, None, ..., None]]

        self.initialisation() # remplissage de la grille de l'ordinateur
        self.dug = set() # si l'on creuse à 0, 0 alors self.dug{(0,0)}

    def initialisation(self):
        bombs_planted = 0

        # placement des bombes
        while bombs_planted < self.num_bombs:
            # définition localisation de la bombe
            col = random.randint(0, self.dim_size-1)
            row = random.randint(0, self.dim_size-1)

            if self.board[row][col] == "bo":
                # on a déja planté une bombe ici donc l'on continue
                continue

            self.board[row][col] = "bo" # on plante la bombe
            bombs_planted += 1

        # remplissage des cases
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == "bo":
                    continue
                self.board[r][c] = str(self.bombs_around(r, c))

    def bombs_around(self, row, col):
        # on fait la somme de toutes les bombes sur les cases voisines
        # top left: (row-1, col-1)
        # top middle: (row-1, col)
        # top right: (row-1, col+1)
        # left: (row, col-1)
        # right: (row, col+1)
        # bottom left: (row+1, col-1)
        # bottom middle: (row+1, col)
        # bottom right: (row+1, col+1)

        # remplissage des cases
        num_bombs_around = 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col:
                    # localisation de base
                    continue
                if self.board[r][c] == "bo":
                    num_bombs_around += 1
        return num_bombs_around

    def dig(self, row, col):
        # on creuse à cette localisation
        # retourne True ou False si l'on creuse sur une bombe

        # quelques scénarios:
        # creuser une bombe -> game over
        # creuser sur une case autre que 0 ou une bombe -> fini de creuser
        # creuser sur une case 0 -> on creuse les voisins récursivement

        self.dug.add((row, col)) # on note que l'on a creusé ici
        self.visible_board[row][col] = str(self.board[row][col]) # on creuse la case

        if self.board[row][col] == "bo":
            self.visible_board[row][col] = 'box'
            self.board[row][col] = "box"
            return False
        elif int(self.board[row][col]) > 0:
            return True

        # self.board[row][col] == 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) in self.dug:
                    continue # on ne creuse ou on a déja creusé
                self.dig(r,c)

        # si notre trou initial n'a pas touché de bombes, alors on ne doit pas toucher une bombe ici
        return True

    def flag(self, row, col):
        # l'utilisateur met un drapeau sur les cases où il pense qu'il y a une bombe
        if self.visible_board[row][col] == '--':
            self.visible_board[row][col] = "D"
            return True
        elif self.visible_board[row][col] == "D":
            # l'utilisateur retire le drapeau
            self.visible_board[row][col] = '--'
            return True


def load_Images():
    # on charge les images du projet, chaque type de cases correspond à une image
    global SQ_SIZE
    pieces = ['0', '1', '2', '3', '4', '5', '6', '7', '8', 'bo', '--', 'D', 'box']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("Images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


def main(board, dim):
    global SQ_SIZE
    global DIMENSION
    WIDTH = HEIGHT = dim
    DIMENSION = board.dim_size # nombre de case dans la grille
    SQ_SIZE = HEIGHT // DIMENSION # dimension d'une case
    messagebox.showinfo('Minesweeper','Clic Gauche pour creuser \nClic Droit pour planter un drapeau') # commande

    p.init() # initialisation de pygame
    screen = p.display.set_mode((WIDTH, HEIGHT)) # création de la fenêtre
    p.display.set_caption("Minesweeper - Alpha") # titre de la fenêtre
    screen.fill(p.Color("white")) # background de la fenêtre
    load_Images() # chargement des images
    safe = True
    sqSelected = () # case sélectionée par l'utilisateur

    while len(board.dug) < board.dim_size ** 2 - board.num_bombs:
        for e in p.event.get():
            if e.type == p.QUIT:
                safe = False # quite le jeu sil'on clique sur la croix en haut à droite
            elif e.type == p.MOUSEBUTTONDOWN: # détection un clique de la souris
                location = p.mouse.get_pos() # coordonée du clic de l'utilisateur, location[0] = x, location[y] = y
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE

                sqSelected = (row, col)

                # e.button == 1: clic gauche
                # e.button == 3: clic droit

                if e.button == 1:
                    safe = board.dig(row,col) # si c'est valide, on creuse à la case indiqué
                elif e.button == 3:
                    safe = board.flag(row,col) # on plante un drapeau ou on l'enlève

        drawGameState(screen, board) # on dessine les cases correspondant à la grille visible
        p.display.flip() # on actualise la fenêtre

        if not safe:
            # on acreusé une bombe
            break # rip game over


    # 2 façon de finir la boucle
    if safe:
        print("CONGRATULATIONS!!!! YOU ARE VICTORIOUS!")
        messagebox.showinfo('Minesweeper','CONGRATULATIONS!!!! YOU ARE VICTORIOUS!') # alertbox
        p.quit() # quitte la fenêtre
    else:
        drawEnd(screen, board) # on révèle la position des bombes
        p.display.flip() # on actualise la grille de jeu
        print("SORRY GAME OVER :(")
        messagebox.showinfo('Minesweeper','SORRY GAME OVER :(') # alertbox
        p.quit() # quitte la fenêtre


def drawGameState(screen, gs):
    drawPieces(screen, gs.visible_board) # dessine les cases de la grille

def drawEnd(screen, gs):
    drawPieces(screen, gs.board) # dessine les cases de la grille remplie dès le début

def drawPieces(screen, board):
    global DIMENSION
    for r in range(DIMENSION): # check toutes les cases une par une
        for c in range(DIMENSION):
            piece = board[r][c]
            screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE)) # affiche le png correspondant à la case
