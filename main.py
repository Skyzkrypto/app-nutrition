# imports

from tkinter import *
from PIL import Image, ImageTk

# dimentions

hauteur = 720
largeur = 1080

# fen calendrier

calendrier = Tk()

calendrier.title("Calendrier")
calendrier.geometry("1080x720")
calendrier.minsize(largeur, hauteur)
calendrier.maxsize(largeur, hauteur)

# Charger l'image avec PIL
fond = Image.open("/Users/alexis/Documents/Python/app nutrition/fond.png")
bg = ImageTk.PhotoImage(fond)
back = Label(calendrier, image=bg)
back.pack()

# frame

frame_semaine1 = Frame(calendrier)
frame_semaine1.pack(side="left")

frame_semaine2 = Frame(calendrier)
frame_semaine2.pack(anchor="center")

frame_semaine3 = Frame(calendrier)
frame_semaine3.pack(side="right")

# boucle main

calendrier.mainloop()