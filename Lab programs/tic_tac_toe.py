import math
MAX="O"
MIN="X"

def terminal_test(board):
    return ( check_winner(board,MAX) or check_winner(board,MIN) or " " not in board)
def utility(board):
    if check_winner(board,MAX):
        return 1
    elif check_winner(board,MIN):
        return -1
    else:
        return 0
def print_board(board):
    print()
    for i in range(0,9,3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]}")
        if i<6:
            print("---+---+---")
    print()

def check_winner(state,player):
    winning_combo=[
        (0,1,2),
        (3,4,5),
        (6,7,8),
        (0,3,6),
        (1,4,7),
        (2,5,8),
        (0,4,8),
        (2,4,6)
    ]
    for a,b,c in winning_combo:
        if state[a]==state[b]==state[c]==player:
            return True
    return False

def actions(board):
    return [i for i in range(9) if board[i]==" "]

def result(board,action,player):
    new_board=board.copy()
    new_board[action]=player
    return new_board

def max_value(board):
    if terminal_test(board):
        return utility(board)
    v=-math.inf
    for action in actions(board):
        v=max(v,min_value(result(board,action,MAX)))
    return v
def min_value(board):
    if terminal_test(board):
        return utility(board)
    v=math.inf
    for action in actions(board):
        v=min(v,max_value(result(board,action,MIN)))
    return v

def minimax_decision(board):
    best_action=None
    best_value=-math.inf
    for action in actions(board):
        value = min_value(result(board,action,MAX))
        if value>best_value:
            best_value=value
            best_action=action

    return best_action

board = [" "] * 9

print("TIC-TAC-TOE")
print("You = X")
print("AI  = O")

while not terminal_test(board):
    print_board(board)
    while True:
        try:
            move = int(input("Enter a number from 1 to 9:"))-1

            if move in actions(board):
                break
            else:
                print("Invalid move try again")
        except ValueError:
            print("Please enter a nmber from 1 to 9")
    board[move]=MIN
    if terminal_test(board):
        break
    print("AI is thinking ")
    ai_move=minimax_decision(board)
    board[ai_move]=MAX
    print(f"Ai move is : {ai_move+1}")
print_board(board)
if check_winner(board,MIN):
    print("Human wins")
elif check_winner(board,MAX):
    print("Ai wins")
else:
    print("Game is a draw")