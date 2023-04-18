import tkinter as tk
from tkinter import messagebox

# Définition des constantes pour la grille
GRID_WIDTH = 7
GRID_HEIGHT = 6
WINNING_LENGTH = 4

# Classe pour le jeu de Puissance 4
class Puissance4:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Puissance 4")
        self.canvas = tk.Canvas(self.window, width=600, height=500)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.play)
        self.new_game()

    def new_game(self):
        self.turn = "Joueur 1"
        self.grid = [["" for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                x1 = col * 80 + 100
                y1 = row * 80 + 100
                x2 = x1 + 80
                y2 = y1 + 80
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
                if self.grid[row][col] == "Joueur 1":
                    self.canvas.create_oval(x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill="red")
                elif self.grid[row][col] == "Joueur 2":
                    self.canvas.create_oval(x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill="yellow")
        self.canvas.create_text(300, 50, text=self.turn, font=("Helvetica", 24))

    def play(self, event):
        if self.turn == "Joueur 1":
            player = "Joueur 1"
            color = "red"
        else:
            player = "Joueur 2"
            color = "yellow"
        col = event.x // 80
        if self.is_valid_move(col):
            row = self.get_next_empty_row(col)
            self.grid[row][col] = player
            self.draw_board()
            if self.check_winner(row, col):
                messagebox.showinfo("Fin de partie", f"{player} a gagné !")
                self.new_game()
                return
            if self.is_full():
                messagebox.showinfo("Fin de partie", "Match nul !")
                self.new_game()
                return
            self.switch_turn()

    def is_valid_move(self, col):
        return self.grid[0][col] == ""

    def get_next_empty_row(self, col):
        for row in range(GRID_HEIGHT - 1, -1, -1):
            if self.grid[row][col] == "":
                return row

    def switch_turn(self):
        if self.turn == "Joueur 1":
            self.turn = "Joueur 2"
        else:
            self.turn = "Joueur 1"

    def is_full(self):
        for col in range(GRID_WIDTH):
            if self.grid[0][col] == "":
                return False
        return True

    def check_winner(self, row, col):
        player = self.grid[row][col]
        # Vérification horizontale
        count = 1
        for i in range(col - 1, -1, -