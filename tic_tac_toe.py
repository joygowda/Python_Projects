"""
Simple automated tic tac toe game for Python 3
coded by Joy Dhairyalakshmi Gowda
"""
import random
import time

# Constants for the game
COMPUTER = 1
HUMAN = 2
SIDE = 3
COMPUTERMOVE = 'O'
HUMANMOVE = 'X'

# Function to initialise the game / Tic-Tac-Toe board
def initialise():
    board = [[' ' for _ in range(SIDE)] for _ in range(SIDE)]
    moves = [i for i in range(SIDE*SIDE)]
    random.shuffle(moves)
    return board, moves

# Function to print the Tic-Tac-Toe board
def showBoard(board):
    print("\n\n")
    print("\t\t\t  {} | {}  | {}  ".format(board[0][0], board[0][1], board[0][2]))
    print("\t\t\t--------------")
    print("\t\t\t  {} | {}  | {}  ".format(board[1][0], board[1][1], board[1][2]))
    print("\t\t\t--------------")
    print("\t\t\t  {} | {}  | {}  \n\n".format(board[2][0], board[2][1], board[2][2]))

# Function to show the instructions
def showInstructions():
    print("\t\t\t  Tic-Tac-Toe\n\n")
    print("Choose a cell numbered from 1 to 9 as below and play\n\n")
    print("\t\t\t  1 | 2  | 3  ")
    print("\t\t\t--------------")
    print("\t\t\t  4 | 5  | 6  ")
    print("\t\t\t--------------")
    print("\t\t\t  7 | 8  | 9  \n\n")
    print("-\t-\t-\t-\t-\t-\t-\t-\t-\t-\n\n")

# Function to declare the winner of the game
def declareWinner(whoseTurn):
    if whoseTurn == COMPUTER:
        print("COMPUTER has won")
    else:
        print("HUMAN has won")

# Functions to check if any of the rows, columns, or diagonals have been crossed
def rowCrossed(board):
    for i in range(SIDE):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != ' ':
            return True
    return False

def columnCrossed(board):
    for i in range(SIDE):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != ' ':
            return True
    return False

def diagonalCrossed(board):
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != ' ':
        return True
    return False

# Function to check if the game is over
def gameOver(board):
    return rowCrossed(board) or columnCrossed(board) or diagonalCrossed(board)

# Function to play Tic-Tac-Toe
def playTicTacToe(whoseTurn):
    board, moves = initialise()
    showInstructions()
    moveIndex = 0
    while not gameOver(board) and moveIndex != SIDE*SIDE:
        if whoseTurn == COMPUTER:
            x = moves[moveIndex] // SIDE
            y = moves[moveIndex] % SIDE
            board[x][y] = COMPUTERMOVE
            print("COMPUTER has put a {} in cell {}".format(COMPUTERMOVE, moves[moveIndex]+1))
            showBoard(board)
            moveIndex += 1
            whoseTurn = HUMAN
        elif whoseTurn == HUMAN:
            x = moves[moveIndex] // SIDE
            y = moves[moveIndex] % SIDE
            board[x][y] = HUMANMOVE
            print("HUMAN has put a {} in cell {}".format(HUMANMOVE, moves[moveIndex]+1))
            showBoard(board)
            moveIndex += 1
            whoseTurn = COMPUTER
    if not gameOver(board) and moveIndex == SIDE*SIDE:
        print("It's a draw")
    else:
        if whoseTurn == COMPUTER:
            whoseTurn = HUMAN
        elif whoseTurn == HUMAN:
            whoseTurn = COMPUTER
        declareWinner(whoseTurn)

# Driver function
if __name__ == "__main__":
    # Let us play the game with COMPUTER starting first
    playTicTacToe(COMPUTER)
