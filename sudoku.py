# import
import tkinter as tk
import random as rd
import numpy as np
import copy as cp


# variables
en_jeu = False

HAUTEUR = 650
LARGEUR = 650


# fonction
def generation():
    """Genere une liste 9x9 complète de manière aléatoire"""
    sudoku = list()
    gauche, milieu, droite = [1, 2], [3, 4, 5], [6, 7, 8]
    nombre = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    rd.shuffle(nombre)
    m, d = rd.choice(milieu), rd.choice(droite)
    print(m, d)
    milieu.remove(m)
    droite.remove(d)
    print(milieu, droite)
    liste1, liste2 = list(np.roll(nombre, m)), list(np.roll(nombre, d))
    print(nombre, liste1, liste2)
    g, m, d = rd.choice(gauche), rd.choice(milieu), rd.choice(droite)
    print(g, m, d)
    gauche.remove(g)
    milieu.remove(m)
    droite.remove(d)
    print(gauche, milieu, droite)
    liste3, liste4 = list(np.roll(nombre, g)), list(np.roll(nombre, m))
    liste5 = list(np.roll(nombre, d))
    print(nombre, liste1, liste2, liste3, liste4, liste5)
    liste6 = list(np.roll(nombre, gauche[0]))
    liste7 = list(np.roll(nombre, gauche[0]))
    liste8 = list(np.roll(nombre, droite[0]))
    sudoku.append(nombre), sudoku.append(liste1), sudoku.append(liste2)
    sudoku.append(liste3), sudoku.append(liste4), sudoku.append(liste5)
    sudoku.append(liste6), sudoku.append(liste7), sudoku.append(liste8)
    return sudoku


def grille():
    """Genere une grille sur l'interface graphique"""
    for i in range(9):
        for j in range(9):
            x, y = (LARGEUR//9)*i, (HAUTEUR//9)*j
            x1, y1 = x+(LARGEUR//9), y+(HAUTEUR//9)
            canvas.create_rectangle(x, y, x1, y1, fill="white",
                                    tags=f"carré_{j}_{i}")
    canvas.create_line(LARGEUR//3, 0, LARGEUR//3, HAUTEUR, width=5)
    canvas.create_line((LARGEUR//3)*2, 0, (LARGEUR//3)*2, HAUTEUR, width=5)
    canvas.create_line(0, HAUTEUR//3, LARGEUR, HAUTEUR//3, width=5)
    canvas.create_line(0, (HAUTEUR//3)*2, LARGEUR, (HAUTEUR//3)*2, width=5)


def rejouer():
    """Permet de relancer une partie (à finir)"""
    canvas.delete('all')
    grille()


def donnecoord(event):
    """Renvoie les coordonnées de l'endroit où on a cliqué (à finir)"""
    print("vous avez clic gauche")


def entrernombre(event):
    """(à finir)"""
    print("entrer presser")


def checkligne(a):
    """Verifie que la ligne respecte les regles du sudoku"""
    nombre = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    k = 0
    for i in range(9):
        if a[i].count(nombre[k]) != 1:
            return False
        k += 1
    return True


def lirecolonne(a):
    """Lit les colonnes sous forme de ligne"""
    acolonne = [[0]*9 for i in range(9)]
    i = 0
    j = 0
    for i in range(9):
        for j in range(9):
            acolonne[i][j] = a[j][i]
    return acolonne


def lirecarre(a):
    """Lit les sous-carrés sous forme de ligne"""
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
    """Verfie que tout le sudoku respecte les regles"""
    return checkligne(a), lirecolonne(checkligne(a)), lirecarre(checkligne(a))


def difficulte(liste, str):
    """Renvoie un sudoku à completer selon la difficulté"""
    copie = cp.deepcopy(liste)
    if str == "facile":
        case = 43
    elif str == "moyen":
        case = 51
    elif str == "difficile":
        case = 56
    for i in range(case):
        while case > 1:
            i, j = rd.randint(0, 8), rd.randint(0, 8)
            if copie[i][j] == 0:
                pass
            else:
                copie[i][j] = 0
                case -= 1
    return liste, copie


# interface graphique
racine = tk.Tk()
racine.title("Sudoku")
canvas = tk.Canvas(racine, height=HAUTEUR, width=LARGEUR, background='white')
tk.Button(racine, text='Grille', command=grille).grid(row=0, column=0)
tk.Button(racine, text='Rejouer', command=rejouer).grid(row=1, column=0)
tk.Label(racine, text="Chiffre à mettre dans\
         la grille\nentre 1 et 9").grid(row=0, column=2)
entry = tk.Entry(racine, width=3).grid(row=1, column=2)
canvas.grid(row=0, column=1, rowspan=10)
canvas.bind('<ButtonRelease-1>', donnecoord)
racine.bind('<Return>', entrernombre)
racine.mainloop()
