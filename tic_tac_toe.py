import tkinter as tk
from tkinter import messagebox
import random
from functools import partial

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Tic-Tac-Toe')
        self.initialize_game()

    def initialize_game(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'O'  # Human player starts first
        self.game_over = False
        self.buttons = []

        # Clear the window and create the game board and control buttons
        for widget in self.root.winfo_children():
            widget.destroy()

        self.create_board()
        self.create_control_buttons()

    def create_board(self):
        for i in range(9):
            action = partial(self.on_click, i)
            btn = tk.Button(self.root, text=' ', font=('normal', 40), height=2, width=5, command=action)
            btn.grid(row=i // 3, column=i % 3)
            self.buttons.append(btn)

    def create_control_buttons(self):
        # Only restart game button is needed
        tk.Button(self.root, text='Restart Game', command=self.initialize_game, font=('normal', 20)).grid(row=3, column=0, columnspan=3, sticky="nsew")

    def on_click(self, index):
        if self.board[index] == ' ' and not self.game_over:
            self.make_move(index, self.current_player)
            if self.check_win(self.current_player):
                messagebox.showinfo("Game Over", "Player Wins!")
                self.game_over = True
                return
            elif ' ' not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.game_over = True
                return
            self.current_player = 'X'  # Switch to computer player
            self.computer_move()

    def make_move(self, index, player):
        self.board[index] = player
        self.buttons[index].config(text=player)

    def check_win(self, player):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if all(self.board[i] == player for i in condition):
                return True
        return False

    def computer_move(self):
        if self.game_over:
            return
        available_moves = [i for i, spot in enumerate(self.board) if spot == ' ']
        move = random.choice(available_moves)
        self.make_move(move, 'X')
        if self.check_win('X'):
            messagebox.showinfo("Game Over", "Computer Wins!")
            self.game_over = True
        elif ' ' not in self.board:
            messagebox.showinfo("Game Over", "It's a draw!")
            self.game_over = True
        else:
            self.current_player = 'O'

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    game = TicTacToe()
    game.run()
