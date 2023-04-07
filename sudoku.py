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

# fonctions et GUI


def generate_sudoku():
    """Create a 9x9 grid with all cells set to 0"""
    grid = [[0 for _ in range(9)] for _ in range(9)]

    """Fill in the diagonal sub-grids with valid values"""
    for i in range(0, 9, 3):
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        rd.shuffle(values)
        for j in range(3):
            for k in range(3):
                grid[i+j][i+k] = values.pop()

    """Solve the partially filled grid"""
    solve_sudoku(grid)

    return grid

def solve_sudoku(grid):
    """Find the next empty cell and try to fill it with a valid value"""
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

    """Check if a value is valid for a given cell"""
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

    """Start solving the grid from the first empty cell"""
    fill_next_empty_cell()

sudoku = generate_sudoku()

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
    """Change 40 to the number of cells to reveal"""
    revealed_cells = rd.sample(range(81), 50)
    for i in range(81):
        emplacement = canvas.coords(liste[i])
        x, y = (emplacement[0]+emplacement[2])/2, (emplacement[1]+emplacement[3])/2
        if i in revealed_cells:
            canvas.create_text(x, y, text=sudoku[i // 9][i % 9], tags="default_number", font=('Arial',17,'bold'))
        else:
            canvas.create_text(x, y, text=" ",font=('Arial',10))
    print(canvas.find_all())


def clic(event):
    global item_id
    if 'item_id' in globals():
        if (80 > item_id or item_id > 85) and ("default_number" not in canvas.gettags(item_id)):
            canvas.itemconfig(item_id, text ="")
            if item_id > 85:
                item_id -= 85
            canvas.itemconfig(item_id, fill="white")
        else:
            item_id = 0
    item_id = event.widget.find_withtag('current')[0]
    if 80 > item_id or item_id > 85:
        if item_id <= 80:
            item_id += 85
            if "default_number" not in canvas.gettags(item_id):
                item_id -= 85
                canvas.itemconfig(item_id, fill="grey")
                item_id += 85
                canvas.itemconfig(item_id, text="Input:")
                return item_id
            else:
                item_id = 0



def texte_chiffre(e):
    global item_id
    additional_keys = ["ampersand","eacute","quotedbl","apostrophe","parenleft","minus","egrave","underscore","ccedilla"]
    key = str(e.keysym)
    if key in additional_keys:
        key = str(additional_keys.index(key) + 1)
    elif 'F' in key:
        key = key[1]
    elif key in ["space","Return","BackSpace","Escape","Delete"]:
        key = ''
    canvas.itemconfig(item_id, text = key)
    item_id -= 85
    canvas.itemconfig(item_id, fill="white")
    item_id = 0
    return item_id


racine = tk.Tk()
racine.title("SUDOKU")
canvas = tk.Canvas(racine, height=COTE, width=COTE, bg="white")
canvas.grid(row=0, column=1, rowspan=10)

grille()
texte()

canvas.bind('<ButtonRelease-1>', clic)

for i in range(1,10):
    racine.bind(str(i), texte_chiffre)
    racine.bind('<F'+str(i)+'>', texte_chiffre)
for i in ["&","<eacute>",'"',"'","(","-","<egrave>","_","<ccedilla>","<space>","<Delete>","<BackSpace>","<Escape>","<Return>"]:
    racine.bind(i,texte_chiffre)

racine.mainloop()