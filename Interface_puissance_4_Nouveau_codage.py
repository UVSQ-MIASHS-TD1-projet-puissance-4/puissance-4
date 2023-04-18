import tkinter as tk

root = tk.Tk() # Correction : Ajouter les parenthèses pour créer une instance de la classe Tk()
root.title("Puissance 4") # Correction : Ajouter un titre à la fenêtre
root.geometry("500x500")

canvas = tk.Canvas(root, width=400, height=400, bg='blue')
canvas.pack()

for i in range(7):
    canvas.create_line(i*50+50, 50, i*50+50, 350)

for i in range(6):
    canvas.create_line(50, i*50+50, 350, i*50+50)

buttons = []

def play(col):
    global player
    # Vérifiez si la colonne est pleine.
    if board[0][col] != 0:
        return
    # Placez le jeton dans la colonne.
    row = 0
    while row < 5 and board[row+1][col] == 0:
        row += 1
        board[row][col] = player
        # Dessinez le jeton sur le canevas.
        x = col * 50 + 75
        y = row * 50 + 75
        canvas.create_oval(x-20, y-20, x+20, y+20, fill=color[player])
    # Passez au joueur suivant.
    player = 3 - player

for i in range(7):
    button = tk.Button(root, text='Jouer', command=lambda col=i: play(col))
    button.pack()
    buttons.append(button)

def check_win(board, player):
    # Vérification horizontale
    for i in range(6):
        for j in range(4):
            if board[i][j] == player and board[i][j+1] == player and board[i][j+2] == player and board[i][j+3] == player:
                return True
    # Vérification verticale
    for i in range(7):
        for j in range(3):
            if board[j][i] == player and board[j+1][i] == player and board[j+2][i] == player and board[j+3][i] == player:
                return True
    # Vérification diagonale (bas gauche vers haut droit)
    for i in range(3):
        for j in range(4):
            if board[i][j] == player and board[i+1][j+1] == player and board[i+2][j+2] == player and board[i+3][j+3] == player:
                return True
    # Vérification diagonale (haut gauche vers bas droit)
    for i in range(3, 6):
        for j in range(4):
            if board[i][j] == player and board[i-1][j+1] == player and board[i-2][j+2] == player and board[i-3][j+3] == player:
                return True
    return False

global player
player = 1
board = [[0 for _ in range(7)] for _ in range(6)]
color = {1: 'red', 2: 'yellow'}

root.mainloop()