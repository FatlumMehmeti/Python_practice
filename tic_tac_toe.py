from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    
    for row in board:
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|  ",row[0],"  |  ",row[1],"  |  ",row[2],"  |")
        print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    free = make_list_of_free_fields(board)
    valid = False
    while not valid:
        try:
            move = int(input("Enter your move: "))
            if move < 1 or move > 9:
                print("Invalid move. Choose between 1 and 9.")
                continue
            row, col = (move-1)//3, (move-1)%3
            if (row, col) in free:
                board[row][col] = "X"
                valid = True
            else:
                print("That square is already taken!")
        except ValueError:
            print("Please enter a valid number (1–9).")


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free = []
    for r in range(3):
        for c in range(3):
            if board[r][c] not in ['O', 'X']:
                free.append((r, c))
    return free


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    # Rows
    for i in range(3):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            return True
    # Columns
    for i in range(3):
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            return True
    # Diagonals
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    return False


def draw_move(board):
    # The function draws the computer's move and updates the board.
    free = make_list_of_free_fields(board)
    if free:
        row, col = free[randrange(len(free))]
        board[row][col] = "O"


# Starting the game
print("Let's play Tic Tac Toe!")
board = [[1,2,3],
         [4,5,6],
         [7,8,9]]

display_board(board)

while True:
    enter_move(board)
    display_board(board)
    if victory_for(board, "X"):
        print("You won!")
        break
    elif not make_list_of_free_fields(board):
        print("It's a tie!")
        break

    draw_move(board)
    display_board(board)
    if victory_for(board, "O"):
        print("Computer won!")
        break
    elif not make_list_of_free_fields(board):
        print("It's a tie!")
        break