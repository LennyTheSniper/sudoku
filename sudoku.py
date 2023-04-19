# import
import tkinter as tk
import random as rd
import copy as cp
import time as tm

# variables

# taille du canvas
COTE = 650

# taille du canvas divisé par 3
COTE3 = COTE//3

# taille du canvas divisé par 9
COTE9 = COTE//9

# identifiant de l'objet sur lequel on a cliqué
item_id = 0

# solution du sudoku
solution = None

# sudoku
sudoku = None

# copie du sudoku en debut de partie
copie_sudoku = None

# temps auquel la partie débute
debut = 0

# nombre d'erreurs
erreur = 0

# fonctions


def grille():
    """ Trace les lignes du sudoku """
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
    """Met une zone de texte dans tous les carrés du sudoku """
    liste = canvas.find_all()
    for i in range(81):
        emplacement = canvas.coords(liste[i])
        x = (emplacement[0]+emplacement[2])/2
        y = (emplacement[1]+emplacement[3])/2
        canvas.create_text(x, y, text="", font=("Arial", 17, "bold"))
    # print(canvas.find_all())


def clic(event):
    """ Selectionne un carre dans le sudoku """
    global item_id
    if item_id != 0:
        enlever_aide()
    item_id = event.widget.find_withtag('current')[0]
    if item_id in [82, 83, 84, 85]:
        item_id = 0
    # print(item_id)
    if item_id > 82:
        item_id -= 85
    # print(item_id)
    canvas.itemconfig(item_id, fill="grey")
    item_id += 85
    textelabel.set("f1-f9 pour chiffre de 1 à 9 et f10 pour effacer")
    # print(item_id)
    return item_id


def un(event):
    """ Met un 1 sur la grille du sudoku et sur l'interface graphique
        et verifie si la partie est finie """
    global item_id, solution, sudoku, erreur
    canvas.itemconfig(item_id, text="1")
    item_id -= 85
    if item_id % 9 == 0:
        i, j = item_id//9-1, 8
    else:
        i, j = item_id//9, item_id % 9 - 1
    if solution[i][j] == 1:
        canvas.itemconfig(item_id, fill="white")
        item_id = 0
        sudoku[i][j] = 1
        if solution == sudoku:
            fin()
    else:
        canvas.itemconfig(item_id, fill="red")
        item_id = 0
        erreur += 1
    return item_id, solution, sudoku, erreur


def deux(event):
    """ Met un 2 sur la grille du sudoku et sur l'interface graphique
        et verifie si la partie est finie """
    global item_id, solution, sudoku, erreur
    canvas.itemconfig(item_id, text="2")
    item_id -= 85
    if item_id % 9 == 0:
        i, j = item_id//9-1, 8
    else:
        i, j = item_id//9, item_id % 9 - 1
    if solution[i][j] == 2:
        canvas.itemconfig(item_id, fill="white")
        item_id = 0
        sudoku[i][j] = 2
        if solution == sudoku:
            fin()
    else:
        canvas.itemconfig(item_id, fill="red")
        item_id = 0
        erreur += 1
    return item_id, solution, sudoku, erreur


def trois(event):
    """ Met un 3 sur la grille du sudoku et sur l'interface graphique
        et verifie si la partie est finie """
    global item_id, solution, sudoku, erreur
    canvas.itemconfig(item_id, text="3")
    item_id -= 85
    if item_id % 9 == 0:
        i, j = item_id//9-1, 8
    else:
        i, j = item_id//9, item_id % 9 - 1
    if solution[i][j] == 3:
        canvas.itemconfig(item_id, fill="white")
        item_id = 0
        sudoku[i][j] = 3
        if solution == sudoku:
            fin()
    else:
        canvas.itemconfig(item_id, fill="red")
        item_id = 0
        erreur += 1
    return item_id, solution, sudoku, erreur


def quatre(event):
    """ Met un 4 sur la grille du sudoku et sur l'interface graphique
        et verifie si la partie est finie """
    global item_id, solution, sudoku, erreur
    canvas.itemconfig(item_id, text="4")
    item_id -= 85
    if item_id % 9 == 0:
        i, j = item_id//9-1, 8
    else:
        i, j = item_id//9, item_id % 9 - 1
    if solution[i][j] == 4:
        canvas.itemconfig(item_id, fill="white")
        item_id = 0
        sudoku[i][j] = 4
        if solution == sudoku:
            fin()
    else:
        canvas.itemconfig(item_id, fill="red")
        item_id = 0
        erreur += 1
    return item_id, solution, sudoku, erreur


def cinq(event):
    """ Met un 5 sur la grille du sudoku et sur l'interface graphique
        et verifie si la partie est finie """
    global item_id, solution, sudoku, erreur
    canvas.itemconfig(item_id, text="5")
    item_id -= 85
    if item_id % 9 == 0:
        i, j = item_id//9-1, 8
    else:
        i, j = item_id//9, item_id % 9 - 1
    if solution[i][j] == 5:
        canvas.itemconfig(item_id, fill="white")
        item_id = 0
        sudoku[i][j] = 5
        if solution == sudoku:
            fin()
    else:
        canvas.itemconfig(item_id, fill="red")
        item_id = 0
        erreur += 1
    return item_id, solution, sudoku, erreur


def six(event):
    """ Met un 6 sur la grille du sudoku et sur l'interface graphique
        et verifie si la partie est finie """
    global item_id, solution, sudoku, erreur
    canvas.itemconfig(item_id, text="6")
    item_id -= 85
    if item_id % 9 == 0:
        i, j = item_id//9-1, 8
    else:
        i, j = item_id//9, item_id % 9 - 1
    if solution[i][j] == 6:
        canvas.itemconfig(item_id, fill="white")
        item_id = 0
        sudoku[i][j] = 6
        if solution == sudoku:
            fin()
    else:
        canvas.itemconfig(item_id, fill="red")
        item_id = 0
        erreur += 1
    return item_id, solution, sudoku, erreur


def sept(event):
    """ Met un 7 sur la grille du sudoku et sur l'interface graphique
        et verifie si la partie est finie """
    global item_id, solution, sudoku, erreur
    canvas.itemconfig(item_id, text="7")
    item_id -= 85
    if item_id % 9 == 0:
        i, j = item_id//9-1, 8
    else:
        i, j = item_id//9, item_id % 9 - 1
    if solution[i][j] == 7:
        canvas.itemconfig(item_id, fill="white")
        item_id = 0
        sudoku[i][j] = 7
        if solution == sudoku:
            fin()
    else:
        canvas.itemconfig(item_id, fill="red")
        item_id = 0
        erreur += 1
    return item_id, solution, sudoku, erreur


def huit(event):
    """ Met un 8 sur la grille du sudoku et sur l'interface graphique
        et verifie si la partie est finie """
    global item_id, solution, sudoku, erreur
    canvas.itemconfig(item_id, text="8")
    item_id -= 85
    if item_id % 9 == 0:
        i, j = item_id//9-1, 8
    else:
        i, j = item_id//9, item_id % 9 - 1
    if solution[i][j] == 8:
        canvas.itemconfig(item_id, fill="white")
        item_id = 0
        sudoku[i][j] = 8
        if solution == sudoku:
            fin()
    else:
        canvas.itemconfig(item_id, fill="red")
        item_id = 0
        erreur += 1
    return item_id, solution, sudoku, erreur


def neuf(event):
    """ Met un 9 sur la grille du sudoku et sur l'interface graphique
        et verifie si la partie est finie"""
    global item_id, solution, sudoku, erreur
    canvas.itemconfig(item_id, text="9")
    # print(item_id)
    item_id -= 85
    # print(item_id)
    if item_id % 9 == 0:
        i, j = item_id//9-1, 8
    else:
        i, j = item_id//9, item_id % 9 - 1
    # print((i, j))
    # for l in solution:
    #    print(l)
    # print(solution[i][j])
    if solution[i][j] == 9:
        canvas.itemconfig(item_id, fill="white")
        item_id = 0
        sudoku[i][j] = 9
        if solution == sudoku:
            fin()
    else:
        canvas.itemconfig(item_id, fill="red")
        item_id = 0
        erreur += 1
    return item_id, solution, sudoku, erreur


def effacer(event):
    """ Efface sur l'interface graphique le nombre sur l'interface graphique
        et verifie si la partie est finie"""
    global item_id
    canvas.itemconfig(item_id, text="")
    item_id -= 85
    canvas.itemconfig(item_id, fill="white")
    item_id = 0
    return item_id


def generatesudoku():
    """ Génere un sudoku """
    global solution
    # Create a 9x9 grid with all cells set to 0
    grid = [[0 for _ in range(9)] for _ in range(9)]

    # Fill in the diagonal sub-grids with valid values
    for i in range(0, 9, 3):
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        rd.shuffle(values)
        for j in range(3):
            for k in range(3):
                grid[i+j][i+k] = values.pop()

    # Solve the partially filled grid
    solve_sudoku(grid)
    solution = cp.deepcopy(grid)
    return solution


def solve_sudoku(grid):
    """ Resout un sudoku """
    # Find the next empty cell and try to fill it with a valid value
    def fill_next_empty_cell():
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    for value in range(1, 10):
                        if is_valid(i, j, value):
                            grid[i][j] = value
                            if fill_next_empty_cell():
                                return True
                            grid[i][j] = 0
                    return False
        return True

    # Check if a value is valid for a given cell
    def is_valid(row, col, value):
        for i in range(9):
            if grid[row][i] == value or grid[i][col] == value:
                return False
        subgrid_row = (row // 3) * 3
        subgrid_col = (col // 3) * 3
        for i in range(subgrid_row, subgrid_row+3):
            for j in range(subgrid_col, subgrid_col+3):
                if grid[i][j] == value:
                    return False
        return True

    # Start solving the grid from the first empty cell
    fill_next_empty_cell()


def case_vide():
    """ Prend la solution du sudoku et renvoie un sudoku avec des trous """
    global solution, sudoku, copie_sudoku
    sudoku = cp.deepcopy(solution)
    random = rd.randint(81//3, 81//2)
    for k in range(random):
        i, j = rd.randint(0, 8), rd.randint(0, 8)
        sudoku[i][j] = 0
    copie_sudoku = cp.deepcopy(sudoku)
    return sudoku, copie_sudoku


def commencer():
    """ Initialise le sudoku et le timer """
    generatesudoku()
    case_vide()
    mise_en_place()
    temps()
    textelabel.set("Bon jeu à vous")


def annuler():
    """ Annule la partie en cours et reinitialise toutes les variables """
    global solution, sudoku, copie_sudoku, item_id, debut, erreur
    solution, sudoku, copie_sudoku = None, None, None
    item_id, debut, erreur = 0, 0, 0
    textelabel.set("Appuyer sur le bouton Commencer pour recommencer")
    for i in range(1, 82):
        canvas.itemconfig(i, fill="white")
        canvas.itemconfig(85+i, text="")
    return solution, sudoku, copie_sudoku, item_id, debut, erreur


def sauvegarder():
    """ Sauvegarde la partie en cours dans un fichier
        texte (écrase la sauvegarde précédente) """
    global solution, sudoku, copie_sudoku
    partie = str([solution, sudoku, copie_sudoku])
    with open("save.txt", "w") as fichier:
        fichier.write(partie)
    textelabel.set("Partie Sauvegardée")


def charger():
    """ Charge une partie sauvegardée """
    global solution, sudoku, copie_sudoku
    with open("save.txt", "r") as fichier:
        partie = eval(fichier.readline())
    # print(type(partie))
    solution = partie[0]
    sudoku = partie[1]
    copie_sudoku = partie[2]
    for i in range(1, 82):
        canvas.itemconfig(i, fill="white")
        canvas.itemconfig(85+i, text="")
    mise_en_place()
    textelabel.set("Partie Chargée")
    return solution, sudoku, copie_sudoku


def aide():
    """ Indique les cases pré-remplies en début de partie """
    global copie_sudoku
    textelabel.set("Voici les cases données en début de partie")
    for i in range(82):
        item_id = i
        canvas.itemconfig(item_id, fill="white")
    for i in range(9):
        for j in range(9):
            if copie_sudoku[i][j] == 0:
                pass
            else:
                item_id = (i*9)+(j+1)
                # print(item_id)
                canvas.itemconfig(item_id, fill="light blue")


def aide2():
    """ Indique les cases actuellement vides """
    global sudoku
    for i in range(82):
        item_id = i
        canvas.itemconfig(item_id, fill="white")
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                item_id = (i*9)+(j+1)
                canvas.itemconfig(item_id, fill="pink")


def mise_en_place():
    """ Affiche graphiquement ce qui est contenu dans sudoku """
    global sudoku
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                pass
            else:
                item_id = (i*9)+(j+1)+85
                canvas.itemconfig(item_id, text=str(sudoku[i][j]))


def enlever_aide():
    """ Enleve les aides """
    for i in range(82):
        item_id = i
        canvas.itemconfig(item_id, fill="white")


def fin():
    """ Arrete le timer et renvoie le temps et le nombre d'erreurs """
    global debut, erreur
    maintenant = tm.time()
    textelabel.set("Partie terminée")
    ecart = str(int(maintenant-debut))
    textetimer.set(ecart + " secondes et" + str(erreur) + "erreur(s)")
    with open("temps.txt", "a") as f:
        f.write(ecart + " secondes et" + str(erreur) + " erreur(s)")
    canvas.after(5000, annuler)
    debut, erreur = 0, 0
    return debut, erreur


def temps():
    """ Renvoie le temps du debut de la partie dans une variable debut """
    global debut
    debut = tm.time()
    return debut


# GUI
racine = tk.Tk()
racine.title("SUDOKU")
textelabel = tk.StringVar(racine, "Appuyer sur le bouton Commencer")
textetimer = tk.StringVar(racine, "Votre temps s'affichera ici")
label = tk.Label(racine, textvariable=textelabel).grid(row=0, column=1)
timer = tk.Label(racine, textvariable=textetimer).grid(row=0, column=2)
canvas = tk.Canvas(racine, height=COTE, width=COTE, bg="white")
canvas.grid(row=1, column=1, rowspan=10)
start = tk.Button(racine, text="Commencer", command=commencer)
help = tk.Button(racine, text="Case donnée", command=aide)
help2 = tk.Button(racine, text="Contraintes", command=aide2)
cancel_help = tk.Button(racine, text="Enlever aide", command=enlever_aide)
cancel = tk.Button(racine, text="Annuler la partie", command=annuler)
save = tk.Button(racine, text="Sauvegarder", command=sauvegarder)
load = tk.Button(racine, text="Charger", command=charger).grid(row=2, column=2)
start.grid(row=1, column=0)
help.grid(row=2, column=0)
help2.grid(row=3, column=0)
cancel_help.grid(row=4, column=0)
cancel.grid(row=5, column=0)
save.grid(row=1, column=2)
canvas.bind('<ButtonRelease-1>', clic)
racine.bind('<F1>', un)
racine.bind('<F2>', deux)
racine.bind('<F3>', trois)
racine.bind('<F4>', quatre)
racine.bind('<F5>', cinq)
racine.bind('<F6>', six)
racine.bind('<F7>', sept)
racine.bind('<F8>', huit)
racine.bind('<F9>', neuf)
racine.bind('<F10>', effacer)
grille()
texte()
racine.mainloop()
