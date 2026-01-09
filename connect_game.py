# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 17:52:05 2023

@author: khadija
"""



from pprint import pprint
from tkinter import*

class ConnectGame:
    def __init__(self, inPlay, p1, p2, max_rounds=5):
        self.p1 = p1
        self.p2 = p2
        self.inPlay = inPlay
        self.L = [["-" for i in range(7)] for j in range(6)]
        self.lastInput = [0, 0]
        self.score_p1 = 0
        self.score_p2 = 0
        self.rounds_played = 0
        self.max_rounds = max_rounds
        self.maxScore = 5  

    def showTable(self):
        pprint(self.L)

    def passTo(self):
        if self.inPlay == "X":
            self.inPlay = "O"
        else:
            self.inPlay = "X"

    def fillTurn(self, column):
        for i in range(5, -1, -1):
            if self.L[i][column] == "-":
                self.L[i][column] = self.inPlay
                self.lastInput = [i, column]
                self.showTable()
                fillGraphic(i, column, self.inPlay)

                if self.checkWin():
                    messagebox.showinfo("Frame ended", f"Player {self.inPlay} won!")
                    self.rounds_played += 1
                    if self.inPlay == "X":
                        self.score_p1 += 1
                    else:
                        self.score_p2 += 1

                    # Check if any player has reached the maxScore
                    if self.score_p1 == self.maxScore or self.score_p2 == self.maxScore:
                        show_result_window(self)
                        root.destroy()
                    elif self.rounds_played == self.max_rounds:
                        show_result_window(self)
                        root.destroy()
                    else:
                        self.clear()
                        update_scores()
                else:
                    self.passTo()
                    update_turn_label()
                break

    def clear(self):
        self.L = [["-" for _ in range(7)] for _ in range(6)]
        self.lastInput = [0, 0]
        for i in range(6):
            for j in range(7):
                B[i][j].configure(text="", bg="blue")

    def checkWin(self): 
        
# Check horizontally
        if(self.lastInput[1]==0):
            if(self.L[self.lastInput[1]][0]==self.L[self.lastInput[0]][1]==self.L[self.lastInput[0]][2]==self.L[self.lastInput[0]][3]==self.inPlay):
                return True
        if(self.lastInput[1]==1):
             if(self.L[self.lastInput[0]][0]==self.L[self.lastInput[0]][1]==self.L[self.lastInput[0]][2]==self.L[self.lastInput[0]][3]):
                 return True
             if(self.L[self.lastInput[0]][4]==self.L[self.lastInput[0]][1]==self.L[self.lastInput[0]][2]==self.L[self.lastInput[0]][3]):
                 return True
        if(self.lastInput[1]==2):
             if(self.L[self.lastInput[0]][0]==self.L[self.lastInput[0]][1]==self.L[self.lastInput[0]][2]==self.L[self.lastInput[0]][3]):
                 return True
             if(self.L[self.lastInput[0]][4]==self.L[self.lastInput[0]][1]==self.L[self.lastInput[0]][2]==self.L[self.lastInput[0]][3]):
                 return True
             if(self.L[self.lastInput[0]][4]==self.L[self.lastInput[0]][5]==self.L[self.lastInput[0]][2]==self.L[self.lastInput[0]][3]):
                 return True
        if(self.lastInput[1]==3):
             if(self.L[self.lastInput[0]][0]==self.L[self.lastInput[0]][1]==self.L[self.lastInput[0]][2]==self.L[self.lastInput[0]][3]):
                 return True
             if(self.L[self.lastInput[0]][4]==self.L[self.lastInput[0]][1]==self.L[self.lastInput[0]][2]==self.L[self.lastInput[0]][3]):
                 return True
             if(self.L[self.lastInput[0]][4]==self.L[self.lastInput[0]][5]==self.L[self.lastInput[0]][2]==self.L[self.lastInput[0]][3]):
                 return True
             if(self.L[self.lastInput[0]][4]==self.L[self.lastInput[0]][5]==self.L[self.lastInput[0]][6]==self.L[self.lastInput[0]][3]):
                 return True;
        if(self.lastInput[1]==4):
             if(self.L[self.lastInput[0]][4]==self.L[self.lastInput[0]][5]==self.L[self.lastInput[0]][6]==self.L[self.lastInput[0]][3]):
                 return True
             if(self.L[self.lastInput[0]][4]==self.L[self.lastInput[0]][1]==self.L[self.lastInput[0]][2]==self.L[self.lastInput[0]][3]):
                 return True
             if(self.L[self.lastInput[0]][4]==self.L[self.lastInput[0]][5]==self.L[self.lastInput[0]][2]==self.L[self.lastInput[0]][3]):
                 return True
        if(self.lastInput[1]==5):
             if(self.L[self.lastInput[0]][4]==self.L[self.lastInput[0]][5]==self.L[self.lastInput[0]][6]==self.L[self.lastInput[0]][3]):
                 return True
             if(self.L[self.lastInput[0]][4]==self.L[self.lastInput[0]][5]==self.L[self.lastInput[0]][2]==self.L[self.lastInput[0]][3]):
                 return True
        if(self.lastInput[1]==6):
             if(self.L[self.lastInput[0]][4]==self.L[self.lastInput[0]][5]==self.L[self.lastInput[0]][6]==self.L[self.lastInput[0]][3]):
                 return True
             
# Check vertically       
        if(self.lastInput[0]<3):
              if(self.L[self.lastInput[0]][self.lastInput[1]]==self.L[self.lastInput[0]+1][self.lastInput[1]]==self.L[self.lastInput[0]+2][self.lastInput[1]]==self.L[self.lastInput[0]+3][self.lastInput[1]]):
                  return True 
              
# Check diagonale bottom-right to top-left
        if self.lastInput[0] >= 3 and self.lastInput[1] >= 3:
             if (self.L[self.lastInput[0]][self.lastInput[1]] == self.L[self.lastInput[0]-1][self.lastInput[1]-1] == self.L[self.lastInput[0]-2][self.lastInput[1]-2] == self.L[self.lastInput[0]-3][self.lastInput[1]-3]):
               return True
# Check diagonale bottom-left to top-right
        if self.lastInput[0] >= 3 and self.lastInput[1] <= 3:
             if (self.L[self.lastInput[0]][self.lastInput[1]] == self.L[self.lastInput[0]-1][self.lastInput[1]+1] == self.L[self.lastInput[0]-2][self.lastInput[1]+2] == self.L[self.lastInput[0]-3][self.lastInput[1]+3]):
              return True
# Check diagonale top-left to bottom-right
        if self.lastInput[0] <= 2 and self.lastInput[1] <= 3:
             if (self.L[self.lastInput[0]][self.lastInput[1]] == self.L[self.lastInput[0]+1][self.lastInput[1]+1] == self.L[self.lastInput[0]+2][self.lastInput[1]+2] == self.L[self.lastInput[0]+3][self.lastInput[1]+3]):
               return True
# Check diagonale top-right to bottom-left
        if self.lastInput[0] <= 2 and self.lastInput[1] >= 3:
             if (self.L[self.lastInput[0]][self.lastInput[1]] == self.L[self.lastInput[0]+1][self.lastInput[1]-1] == self.L[self.lastInput[0]+2][self.lastInput[1]-2] == self.L[self.lastInput[0]+3][self.lastInput[1]-3]):
                return True
        return False
    

def update_scores():
    scoreLabel1.config(text=str(c.score_p1))
    scoreLabel2.config(text=str(c.score_p2))


def update_player_labels():
    message_label1.config(text=c.p1)
    message_label2.config(text=c.p2)
    update_turn_label()


def update_turn_label():
    if c.inPlay == "X":
        turn_label.config(text=f"Current Turn: {c.p1}")
    elif c.inPlay == "O":
        turn_label.config(text=f"Current Turn: {c.p2}")
    else:
        turn_label.config(text="Game has not started")


def WriteName():
    p1_name = entry1.get()
    p2_name = entry2.get()
    c.p1 = p1_name
    c.p2 = p2_name
    update_player_labels()
    submit_button.config(state="disabled")  # Disable the Submit Names button
    start_game()

def show_result_window(connect_game):
    result_window = Tk()
    result_window.title("Game Result")

    # Labels to display player names and scores
    Label(result_window, text=f"P1: {connect_game.p1} (Score: {connect_game.score_p1})").grid(row=0, column=0, padx=10, pady=5)
    Label(result_window, text=f"P2: {connect_game.p2} (Score: {connect_game.score_p2})").grid(row=1, column=0, padx=10, pady=5)
    Label(result_window, text=f"maxScore: {connect_game.maxScore}").grid(row=2, column=0, padx=10, pady=5)

    # OK button to close the 2nd window
    ok_button = Button(result_window, text="OK", command=result_window.destroy)
    ok_button.grid(row=3, column=0, pady=10)

    

c = ConnectGame("X", "", "")

root = Tk()

def fillGraphic(row, col, inplay):
    if inplay == "X":
        B[row][col].configure(text="X", bg="red")
    else:
        B[row][col].configure(text="O", bg="yellow")

B = [['-' for _ in range(7)] for _ in range(6)]

for i in range(6):
    for j in range(7):
        B[i][j] = Button(font=("arial", 20), width=3, text="", bg="blue", command=lambda col=j: c.fillTurn(col))
        B[i][j].grid(row=i + 1, column=j)

turn_label = Label(root, font=("arial", 20), text="Current Turn: X")
turn_label.grid(row=0, column=0, columnspan=7)

clear_button = Button(root, text="Clear", command=c.clear)
clear_button.grid(row=7, columnspan=7)

message_label1 = Label(text="p1")
message_label2 = Label(text="p2")
entry1 = Entry()
entry2 = Entry()

nameLabel1 = Label(font=("arial", 20), text="0")
nameLabel2 = Label(font=("arial", 20), text="0")
message_label1.grid(row=8, column=0, columnspan=2)
message_label2.grid(row=8, column=4, columnspan=6)

entry1.grid(row=8, column=0, columnspan=3)
entry2.grid(row=8, column=4, columnspan=3)

submit_button = Button(root, text="Submit Names", command=WriteName)
submit_button.grid(row=9, column=2, columnspan=3)

scoreLabel1 = Label(font=("arial", 15), text="0")
scoreLabel2 = Label(font=("arial", 15), text="0")
scoreLabel1.grid(row=8, column=2)
scoreLabel2.grid(row=8, column=6)


update_scores()
update_player_labels()

mainloop()