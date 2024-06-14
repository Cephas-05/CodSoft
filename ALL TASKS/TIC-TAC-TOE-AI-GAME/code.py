from tkinter import *
import random

# Initialize the main window
root = Tk()
root.geometry("330x550")
root.title("Tic Tac Toe")
root.resizable(0, 0)

# Set up frames and title label
frame1 = Frame(root)
frame1.pack()
titleLabel = Label(frame1, text="Tic Tac Toe", font=("sans", 26), bg="Green", width=16)
titleLabel.grid(row=0, column=0)

optionFrame = Frame(root, bg="beige")
optionFrame.pack()

frame2 = Frame(root, bg="Dark Red")
frame2.pack()

# Game board and initial settings
board = {1: " ", 2: " ", 3: " ",
         4: " ", 5: " ", 6: " ",
         7: " ", 8: " ", 9: " "}

turn = "x"
game_end = False
mode = "singlePlayer"

# Functions to change game mode
def changeModeToSinglePlayer():
    global mode
    mode = "singlePlayer"
    singlePlayerButton["bg"] = "Steel Blue"
    multiPlayerButton["bg"] = "beige"

def changeModeToMultiplayer():
    global mode
    mode = "multiPlayer"
    multiPlayerButton["bg"] = "Steel Blue"
    singlePlayerButton["bg"] = "beige"

# Update the board display
def updateBoard():
    for key in board.keys():
        buttons[key - 1]["text"] = board[key]

# Check for a win
def checkForWin(player):
    win_conditions = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # rows
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # columns
        (1, 5, 9), (3, 5, 7)              # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Check for a draw
def checkForDraw():
    return all(board[i] != " " for i in board.keys())

# Restart the game
def restartGame():
    global game_end
    game_end = False
    for button in buttons:
        button["text"] = " "
    for i in board.keys():
        board[i] = " "
    titleLabel.config(text="Tic Tac Toe")

# Minimax algorithm for the computer's move
def minimax(board, isMaximizing):
    if checkForWin("o"):
        return 1
    if checkForWin("x"):
        return -1
    if checkForDraw():
        return 0
    bestScore = -100 if isMaximizing else 100
    for key in board.keys():
        if board[key] == " ":
            board[key] = "o" if isMaximizing else "x"
            score = minimax(board, not isMaximizing)
            board[key] = " "
            if isMaximizing:
                bestScore = max(score, bestScore)
            else:
                bestScore = min(score, bestScore)
    return bestScore

# Computer's move
def playComputer():
    bestScore = -100
    bestMove = 0
    for key in board.keys():
        if board[key] == " ":
            board[key] = "o"
            score = minimax(board, False)
            board[key] = " "
            if score > bestScore:
                bestScore = score
                bestMove = key
    board[bestMove] = "o"

# Player's move
def play(event):
    global turn, game_end
    if game_end:
        return
    button = event.widget
    clicked = int(button.grid_info()['row'] * 3 + button.grid_info()['column'] + 1)
    if board[clicked] == " ":
        board[clicked] = turn
        updateBoard()
        if checkForWin(turn):
            titleLabel.config(text=f"{turn} wins the game")
            game_end = True
        elif checkForDraw():
            titleLabel.config(text="Game Draw")
            game_end = True
        else:
            turn = "o" if turn == "x" else "x"
            if mode == "singlePlayer" and turn == "o":
                playComputer()
                updateBoard()
                if checkForWin(turn):
                    titleLabel.config(text=f"{turn} wins the game")
                    game_end = True
                elif checkForDraw():
                    titleLabel.config(text="Game Draw")
                    game_end = True
                turn = "x"

# ------ UI --------

# Change Mode buttons
singlePlayerButton = Button(optionFrame, text="SinglePlayer", width=13, height=1, font=("Arial", 15), bg="beige", relief=RAISED, borderwidth=5, command=changeModeToSinglePlayer)
singlePlayerButton.grid(row=0, column=0, columnspan=1, sticky=NW)

multiPlayerButton = Button(optionFrame, text="Multiplayer", width=13, height=1, font=("Arial", 15), bg="beige", relief=RAISED, borderwidth=5, command=changeModeToMultiplayer)
multiPlayerButton.grid(row=0, column=1, columnspan=1, sticky=NW)

# Tic Tac Toe Board buttons
buttons = []
for row in range(3):
    for col in range(3):
        button = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg="Dark Red", relief=RAISED, borderwidth=5)
        button.grid(row=row, column=col)
        button.bind("<Button-1>", play)
        buttons.append(button)

# Restart button
restartButton = Button(frame2, text="Restart Game", width=19, height=1, font=("Arial", 20), bg="beige", relief=RAISED, borderwidth=5, command=restartGame)
restartButton.grid(row=4, column=0, columnspan=3)

root.mainloop()

