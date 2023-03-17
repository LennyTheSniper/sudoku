#import
import tkinter as tk
import random as rd
import numpy as np
import copy as cp


#variables
en_jeu = False

HAUTEUR = 650
LARGEUR = 650

#fonction
def generation():
    sudoku = list()
    gauche, milieu, droite = [1,2], [3,4,5], [6,7,8]
    a = [1,2,3,4,5,6,7,8,9]
    rd.shuffle(a)
    y, z = rd.choice(milieu), rd.choice(droite)
    print(y,z)
    milieu.remove(y)
    droite.remove(z)
    print(milieu, droite)
    a1, a2 = list(np.roll(a, y)), list(np.roll(a, z))
    print(a,a1,a2)
    x, y, z = rd.choice(gauche), rd.choice(milieu), rd.choice(droite)
    print(x,y,z)
    gauche.remove(x)
    milieu.remove(y)
    droite.remove(z)
    print(gauche,milieu,droite)
    a3, a4, a5 = list(np.roll(a,x)), list(np.roll(a, y)), list(np.roll(a, z))
    print(a,a1,a2,a3,a4,a5)
    a6, a7, a8 = list(np.roll(a,gauche[0])), list(np.roll(a, milieu[0])), list(np.roll(a, droite[0]))
    sudoku.append(a), sudoku.append(a1), sudoku.append(a2), sudoku.append(a3), sudoku.append(a4), sudoku.append(a5), sudoku.append(a6), sudoku.append(a7), sudoku.append(a8)
    return sudoku


def grille():
    for i in range(9):
        for j in range(9):
            x, y = (LARGEUR//9)*i, (HAUTEUR//9)*j
            x1, y1 = x+(LARGEUR//9), y+(HAUTEUR//9)
            canvas.create_rectangle(x, y, x1, y1, fill="white", tags=f"carré_{j}_{i}")
    canvas.create_line(LARGEUR//3, 0, LARGEUR//3, HAUTEUR, width=5)
    canvas.create_line((LARGEUR//3)*2, 0, (LARGEUR//3)*2, HAUTEUR, width=5)
    canvas.create_line(0, HAUTEUR//3, LARGEUR, HAUTEUR//3, width=5)
    canvas.create_line(0, (HAUTEUR//3)*2, LARGEUR, (HAUTEUR//3)*2, width=5)


def rejouer():
    canvas.delete('all')
    grille()


def donnecoord(event):
    print("vous avez clic gauche")


def entrernombre(event):
    print("entrer presser")


def checkligne(a):
    nombre = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    k = 0
    for i in range(9):
        if a[i].count(nombre[k]) != 1:
            return False
        k += 1
    return True 


def lirecolonne(a):
    acolonne = [[0]*9 for i in range(9)]
    i = 0
    j = 0
    for i in range(9):
        for j in range(9):
            acolonne[i][j] = a[j][i]
    return acolonne


def lirecarre(a):
    acarre = [[0]*9 for i in range(9)]
    k, l = 0, 0
    while len(acarre[8]) != 8:
        for i in range(3):
            for j in range(3):
                acarre[i][j] = a[k+i][l+j]
        l += 3
        for i in range(3):
            for j in range(3):
                acarre[i][j] = a[k+i][l+j]
        l += 3
        for i in range(3):
            for j in range(3):
                acarre[i][j] = a[k+i][l+j]
        l = 0
        k += 3
        for i in range(3):
            for j in range(3):
                acarre[i][j] = a[k+i][l+j]
        l += 3
        for i in range(3):
            for j in range(3):
                acarre[i][j] = a[k+i][l+j]
        l += 3
        for i in range(3):
            for j in range(3):
                acarre[i][j] = a[k+i][l+j]
        k += 3
        l = 0
        for i in range(3):
            for j in range(3):
                acarre[i][j] = a[k+i][l+j]
        l += 3
        for i in range(3):
            for j in range(3):
                acarre[i][j] = a[k+i][l+j]
        l += 3
        for i in range(3):
            for j in range(3):
                acarre[i][j] = a[k+i][l+j]
    return acarre



def verification(a):
    return checkligne(a), lirecolonne(checkligne(a)), lirecarre(checkligne(a))


def diff(a, str):
    b = cp.deepcopy(a)
    if str == "facile":
        d = 43
    elif str == "moyen":
        d = 51
    elif str == "difficile":
        d = 56
    for i in range(d):
        while d > 1:
            i, j = rd.randint(0,8), rd.randint(0,8)
            if b[i][j] == 0:
                pass
            else:
                b[i][j] = 0
                d -= 1
    return a, b


#interface graphique
racine = tk.Tk()
racine.title("Sudoku")
canvas = tk.Canvas(racine, height=HAUTEUR, width=LARGEUR, background='white')
tk.Button(racine, text='Grille', command=grille).grid(row=0, column=0)
tk.Button(racine, text='Rejouer', command=rejouer).grid(row=1, column=0)
tk.Label(racine, text="Chiffre à mettre dans la grille\nentre 1 et 9").grid(row=0, column=2)
entry = tk.Entry(racine, width=3).grid(row=1, column=2)
canvas.grid(row=0, column=1, rowspan=10)
canvas.bind('<ButtonRelease-1>', donnecoord)
racine.bind('<Return>', entrernombre)
racine.mainloop()