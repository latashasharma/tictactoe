# Initialize board and game variables
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True

# Print the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# Take player input
def playerInput(board):
    while True:
        try:
            inp = int(input("Enter a number 1-9: "))
            if inp < 1 or inp > 9:
                print("Input out of range. Please enter a number from 1 to 9.")
            elif board[inp - 1] == "-":
                board[inp - 1] = currentPlayer
                break
            else:
                print("Oops! That spot is already taken.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number from 1 to 9.")

# Check horizontal wins
def checkHorizontal(board):
    if board[0] == board[1] == board[2] != "-":
        return board[0]
    elif board[3] == board[4] == board[5] != "-":
        return board[3]
    elif board[6] == board[7] == board[8] != "-":
        return board[6]
    return None

# Check vertical wins
def checkRow(board):
    if board[0] == board[3] == board[6] != "-":
        return board[0]
    elif board[1] == board[4] == board[7] != "-":
        return board[1]
    elif board[2] == board[5] == board[8] != "-":
        return board[2]
    return None

# Check diagonal wins
def checkDiag(board):
    if board[0] == board[4] == board[8] != "-":
        return board[0]
    elif board[2] == board[4] == board[6] != "-":
        return board[2]
    return None

# Check for a tie
def checkTie(board):
    if "-" not in board:
        printBoard(board)
        print("It's a tie!")
        return True
    return False

# Check for win
def checkWin(board):
    global winner
    winner = checkDiag(board) or checkHorizontal(board) or checkRow(board)
    if winner:
        printBoard(board)
        print(f"The winner is {winner}!")
        return True
    return False

# Switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"  # Corrected from "0" to "O"
    else:
        currentPlayer = "X"

# Game loop
while gameRunning:
    printBoard(board)
    playerInput(board)
    
    if checkWin(board):
        gameRunning = False
        break
    
    if checkTie(board):
        gameRunning = False
        break

    switchPlayer()
