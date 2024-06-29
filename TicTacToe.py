import tkinter as tk     #using tkinter to refer
from tkinter import messagebox

class TicTacToe:     # creating a class
    def __init__(self):     #initialization using init method
        self.current_player= "X"     # game starting with X
        self.board = [["","",""],["","",""],["","",""]]     #initialize board for the grid of game
        self.window =tk.Tk()     #window initialization with TK() class
        self.window.title("Tic Tac Toe")     #title

        self.buttonsGrid = []     #Empty buttons
        for i in range(3):     #it will have 3 rows and 3 cols
            row = []
            for j in range(3):
                button =tk.Button(self.window, text="", width=20, height=10, command= lambda i=i, j=j:self.make_move(i, j))     #created button
                button.grid(row=i, column=j)     #giving position i is row num and j is col num
                row.append(button)
            self.buttonsGrid. append(row)     #initializing completed till here
    def make_move(self, row, col):     #define make_move method
        if self.board[row][col] == "":     #checking if its empty or occupied
            self.board[row][col]=self.current_player     #replacing with current_player 
            self.buttonsGrid[row][col].config(text=self.current_player)  
            if self.check_winner(self.current_player):     #checking who is the winner
                messagebox.showinfo("GAME OVER" , "THE WINNER IS "+self.current_player)
                self.window.quit()
            elif self.is_draw():     # checking if it is draw
                messagebox.showinfo("Game Over",  "ITS A DRAW ")
                self.window.quit()
            self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_winner(self, player):     #defining check_winner
        for i in range(3):
            if player == self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return True
            if player == self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return True
        if player == self.board[0][0] == self.board[1][1] == self.board[2][2]:
                return True
        if player == self.board[0][2] == self.board[1][1] == self.board[2][0]:
                return True
        return False
    def is_draw(self):     #defining draw 
         for row in self.board:
              if "" in row:
                   return False
              return True
    
    def run(self):     #define run to run using mainloop method which is given by tkinter
        self.window.mainloop()

game =TicTacToe()     #initializing into game var
game.run()     #calling run 





