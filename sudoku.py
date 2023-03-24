# import
import tkinter as tk
import random as rd
import numpy as np
import copy as cp

# variables
COTE = 650
COTE3 = COTE//3
COTE9 = COTE//9
item_id = 0
test = [[6, 2, 5, 8, 4, 3, 7, 9, 1],
[7, 9, 1, 2, 6, 5, 4, 8, 3],
[4, 8, 3, 9, 7, 1, 6, 2, 5],
[8, 1, 4, 5, 9, 7, 2, 3, 6],
[2, 3, 6, 1, 8, 4, 9, 5, 7],
[9, 5, 7, 3, 2, 6, 8, 1, 4],
[5, 6, 9, 4, 3, 2, 1, 7, 8],
[3, 4, 2, 7, 1, 8, 5, 6, 9],
[1, 7, 8, 6, 5, 9, 3, 4, 2]]
test2 = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
 [1, 2, 3, 4, 5, 6, 7, 8, 9],
 [1, 2, 3, 4, 5, 6, 7, 8, 9],
 [1, 2, 3, 4, 5, 6, 7, 8, 9],
 [1, 2, 3, 4, 5, 6, 7, 8, 9],
 [1, 2, 3, 4, 5, 6, 7, 8, 9],
 [1, 2, 3, 4, 5, 6, 7, 8, 9],
 [1, 2, 3, 4, 5, 6, 7, 8, 9],
 [1, 2, 3, 4, 5, 6, 7, 8, 9]]


# fonctions et GUI
def grille():
    for i in range(9):
        for j in range(9):
            x, y = (COTE9)*j, (COTE9)*i
            x1, y1 = x+COTE9, y+COTE9
            canvas.create_rectangle(x, y, x1, y1, fill="white")
    canvas.create_line(COTE3, 0, COTE3, COTE, width=5)
    canvas.create_line(COTE3*2, 0, COTE3*2, COTE, width=5)
    canvas.create_line(0, COTE3, COTE, COTE3, width=5)
    canvas.create_line(0, COTE3*2, COTE, COTE3*2, width=5)


def texte():
    liste = canvas.find_all()
    for i in range(81):
        emplacement = canvas.coords(liste[i])
        x, y = (emplacement[0]+emplacement[2])/2, (emplacement[1]+emplacement[3])/2
        canvas.create_text(x, y, text="test")
    print(canvas.find_all())


def clic(event):
    global item_id
    item_id = event.widget.find_withtag('current')[0]
    print(item_id)
    if item_id > 85:
        item_id -= 85
    print(item_id)
    canvas.itemconfig(item_id, fill="grey")
    item_id += 85
    canvas.itemconfig(item_id, text="")
    print(item_id)
    return item_id


def entrer(event):
    global item_id
    #print(type(saisi.get()))
    canvas.itemconfig(item_id, text=saisi.get())
    #if le chiffre est au bon endroit:
    #    item_id -= 85
    #    canvas.itemconfig(item_id, fill="white")
    #else:
    #    canvas.itemconfig(item_id, fill="red")
    item_id = 0


def verifligne(liste):
    for i in range(len(liste)):
        for j in range(1, len(liste)):
            if liste[i].count(j) != 1:
                return False
    return True


def lirecolonne(liste):
    listecolonne = [[0]*9 for i in range(9)]
    for i in range(9):
        for j in range(9):
            listecolonne[i][j] = liste[j][i]
    return listecolonne


def lirecarre(liste):
    listecarre = list()
    uneliste = list()
    while len(listecarre) < 8:
        for i in range(3):
            for j in range(3):
                uneliste.append(liste[i][j])
        listecarre.append(uneliste)
        uneliste = list()
        for i in range(3):
            for j in range(3, 6):
                uneliste.append(liste[i][j])
        listecarre.append(uneliste)
        uneliste = list()
        for i in range(3):
            for j in range(6, 9):
                uneliste.append(liste[i][j])
        listecarre.append(uneliste)
        uneliste = list()
        for i in range(3,6):
            for j in range(3):
                uneliste.append(liste[i][j])
        listecarre.append(uneliste)
        uneliste = list()
        for i in range(3, 6):
            for j in range(3, 6):
                uneliste.append(liste[i][j])
        listecarre.append(uneliste)
        uneliste = list()
        for i in range(3,6):
            for j in range(6, 9):
                uneliste.append(liste[i][j])
        listecarre.append(uneliste)
        uneliste = list()
        for i in range(6, 9):
            for j in range(3):
                uneliste.append(liste[i][j])
        listecarre.append(uneliste)
        uneliste = list()
        for i in range(6, 9):
            for j in range(3, 6):
                uneliste.append(liste[i][j])
        listecarre.append(uneliste)
        uneliste = list()
        for i in range(6, 9):
            for j in range(6, 9):
                uneliste.append(liste[i][j])
        listecarre.append(uneliste)
    return listecarre


racine = tk.Tk()
racine.title("SUDOKU")
canvas = tk.Canvas(racine, height=COTE, width=COTE, bg="white")
tk.Label(racine, text="Entrez le chiffre juste en dessous").grid(row=0, column=2)
saisi = tk.Entry(racine, width=1)
canvas.grid(row=0, column=1, rowspan=10)
saisi.grid(row=1, column=2)
grille()
texte()
canvas.bind('<ButtonRelease-1>', clic)
racine.bind('<Return>', entrer)
racine.mainloop()
