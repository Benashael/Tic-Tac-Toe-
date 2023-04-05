# This code enables multiplayer tic tac toe game using GUI

# Importing library 
import tkinter as tk
from tkinter import messagebox

# Defining class
class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")

        # Initializing variables
        self.current_player = "X"
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.game_over = False

        # Creating buttons for each square on the board
        self.buttons = []
        for i in range(9):
            button = tk.Button(self.master, text=" ", width=10, height=5,
                               command=lambda idx=i: self.button_click(idx))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

        # Creating a reset button
        reset_button = tk.Button(self.master, text="Reset", command=self.reset)
        reset_button.grid(row=3, column=1)

    def button_click(self, idx):
        # Ignoring button clicks if the game is over or the square is already occupied
        if self.game_over or self.board[idx] != " ":
            return

        # Updating the board and the button text
        self.board[idx] = self.current_player
        self.buttons[idx].config(text=self.current_player)

        # Checking for a winner or tie game
        winner = self.check_for_winner()
        if winner:
            messagebox.showinfo("Winner", f"{winner} wins!")
            self.game_over = True
        elif " " not in self.board:
            messagebox.showinfo("Tie Game", "The game is a tie.")
            self.game_over = True
        else:
            # Switching to the other player's turn
            self.current_player = "O" if self.current_player == "X" else "X"

    def check_for_winner(self):
        # Checking rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2] != " ":
                return self.board[i]

        # Checking columns
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != " ":
                return self.board[i]

        # Checking diagonals
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != " ":
            return self.board[2]

        # No winner
        return None

    def reset(self):
        # Reseting the game
        self.current_player = "X"
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.game_over = False
        for button in self.buttons:
            button.config(text=" ")

# Creating the main window
root = tk.Tk()

# Creating the game
game = TicTacToe(root)

# Starting the main event loop
root.mainloop()
