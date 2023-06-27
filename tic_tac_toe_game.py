#procedure 
# print the board
# Take player input
# check win or Tie
#switch player
#check win and Tie again

#global variable declaration 
board =["-","-","-",
        "-","-","-",
        "-","-","-"]

current_player = "x"
winner = None
gameRunning = True

# printing the game board:

def print_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])
print_board(board)

# Take player input
def player_input(board):
    a = int(input("Enter a number 1-9"))
    if a>=1 and a<=9 and board[a-1]:
        board[a-1] = current_player
    else:
        print("Enter the available sapce !!")


# check Win or Tie
def check_horizon(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def check_vertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
def check_tie(board):
    if "-" not in board:
        print_board(board)
        print("It is a Tie!!!")

def check_win():
    if check_diagonal(board) or check_horizon(board) or check_vertical(board):
        print(f"The winner is {winner}")
    gameRunning = False
    

# Switch player
def switch_player():
    global current_player
    if current_player == "x":
        current_player = "o"
    else:
        current_player = "x"
    
while gameRunning:
    print_board(board)
    player_input(board)
    check_win()
    check_tie(board)
    switch_player()


    