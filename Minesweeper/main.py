                ################################
                ################################
                ##      Projet - Démineur     ##
                ##        Version - 5         ##
                ##    Fichier - Principal     ##
                ## Touches Utiles - BGS / BDS ##
                ##       Luc-Alexandre        ##
                ##         17/10/2021         ##
                ################################
                ################################



# Importation librairie
import pygame as p
import minesweeper as ms # Librairie principale, contient le jeu
from tkinter import *
from tkinter import messagebox


# Création variable globale
root = ""
quickplay_win = ""

def quickPlay():
    # Création menu quickplay, 3 étapes

    global quickplay_win
    root.destroy() # Etape 1: Destruction de l'écran principal

    # Etape 2: Création de la nouvelle fenêtre
    quickplay_win = Tk()
    quickplay_win.geometry("510x400") # fenêtre de 510 px sur 400 px
    quickplay_win.title("Minesweeper - Alpha") # titre de la fenêtre
    quickplay_win["bg"] = "#FFFFFF" # background de la fenêtre (blanc)

    # Etape 3: Création des différents components de la page
    accueil_img = PhotoImage(master = quickplay_win, file="Images/logo.gif") # chargement de l'image principale
    accueil_img_label = Label(quickplay_win, image=accueil_img)
    accueil_img_label.pack(anchor=NW, pady=20, padx=58) # apparition image principale sur l'écran, en haut à gauche de la fenêtre

    button_frame = Frame(quickplay_win, bg="white") # création de la grille pour les boutons
    button_frame.pack()                             # c'est ce qui va nous permettre de mettre les boutons dans l'ordre que l'on veut

    play_button = Button(button_frame, text="Facile", command=easy, width=20, height=5, bg="white") # création bouton dificulté facile
    play_button.grid(row=0, column=0, pady=30, padx=10)

    quick_button = Button(button_frame, text="Moyen", command=medium, width=20, height=5, bg="white") # création bouton dificulté medium
    quick_button.grid(row=0, column=1, pady=10, padx=10)

    quick_button = Button(button_frame, text="Difficile", command=hard, width=20, height=5, bg="white") # création bouton dificulté difficile
    quick_button.grid(row=0, column=2, pady=10, padx=10)


    root.mainloop() # affichage de la fenêtre

def easy():
    # Lancement démineur facile, 3 étapes

    global quickplay_win
    quickplay_win.destroy() # Etape 1: Destruction de l'écran quickplay

    # Etape 2 : lancement du niveau facile
    game = ms.Board(10, 12) # setup de la grille de jeu ms.Board(DIMSIZE, NUM_BOMS)
    ms.main(game, 512) # lancement du jeu

    home() # Etape 3: Reviens sur le menu principale une fois le jeu gagné pou perdu

def medium():
    # Lancement démineur medium, 3 étapes

    global quickplay_win
    quickplay_win.destroy() # Etape 1: Destruction de l'écran quickplay

    # Etape 2 : lancement du niveau medium
    game = ms.Board(18, 45) # setup de la grille de jeu ms.Board(DIMSIZE, NUM_BOMS)
    ms.main(game, 650) # lancement du jeu

    home() # Etape 3: Reviens sur le menu principale une fois le jeu gagné pou perdu

def hard():
    # Lancement démineur difficile, 3 étapes

    global quickplay_win
    quickplay_win.destroy() # Etape 1: Destruction de l'écran quickplay

    # Etape 2 : lancement du niveau difficile
    game = ms.Board(24, 99) # setup de la grille de jeu ms.Board(DIMSIZE, NUM_BOMS)
    ms.main(game, 800) # lancement du jeu

    home() # Etape 3: Reviens sur le menu principale une fois le jeu gagné pou perdu

def play():
    messagebox.showinfo('Minesweeper','Not available in alpha version yet')


def home():
    # Création de l'écran principal, 2 étapes

    global root

    # Etape 1: Création de la fenêtre
    root = Tk()
    root.geometry("400x400") # fenêtre de 400 px sur 400 px
    root.title("Minesweeper - Alpha") # titre de la fenêtre
    root["bg"] = "#FFFFFF" # background de la fenêtre (blanc)

    # Etape 3: Création des différents components de la page
    accueil_img = PhotoImage(master = root, file="Images/logo.gif") # chargement de l'image principale
    accueil_img_label = Label(root, image=accueil_img)
    accueil_img_label.pack(anchor=NW, pady=20, padx=8) # apparition image principale sur l'écran, en haut à gauche de la fenêtre

    button_frame = Frame(root, bg="white") # création de la grille pour les boutons
    button_frame.pack()                    # c'est ce qui va nous permettre de mettre les boutons dans l'ordre que l'on veut

    play_button = Button(button_frame, text="Play", command=play, width=20, height=5, bg="white") # création bouton play
    play_button.grid(row=0, column=0, padx=50, pady=10)

    quick_button = Button(button_frame, text="Quick Play", command=quickPlay, width=20, height=5, bg="white") # création bouton quickplay
    quick_button.grid(row=1, column=0, padx=50, pady=10)

    root.mainloop() # affichage de la fenêtre

home() #lance le menu principal