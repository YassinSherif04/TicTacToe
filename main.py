def print_board(func_board):
    print("     1     2     3   ")
    for i in range(3):
        print("  ^^^^^^^^^^^^^^^^^^^")
        print("{0} |  ".format(i+1),end = '')
        
        for j in range(3):
            print(func_board[i][j],end = '  |  ')
            
        print("\n")
        
    print("  ^^^^^^^^^^^^^^^^^^^")


def next_move(board,symbol):
    row = int(input(symbol+"'s move on row: ")) - 1
    column = int(input(symbol+"'s move on column: ")) - 1
    board[row][column] = symbol


def there_is_win():
    for i in range(3):    
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != '_':
            print("game ends")
            print("the player "+symbol+" wins")
            return True
            
    for j in range(3):    
        if board[0][j] == board[1][j] and board[1][j] == board[2][j] and board[0][j] != '_':
            print("game ends")
            print("the player "+symbol+" wins")
            return True
        
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != '_':
        print("game ends")
        print("the player "+symbol+" wins")
        return True
    
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] != '_':
        print("game ends")
        print("the player "+symbol+" wins")
        return True
    
    return False


def there_is_tie():
    board_is_full = True
    for i in range(3):
        if board[i].count('_') > 0:
            board_is_full = False
            break
        
    if board_is_full and not there_is_win():
        print("game ends")
        print("there is a tie")
        return True
    return False


if __name__ == '__main__':

    board = [["_" for j in range(3)] for i in range(3)] #board is set

    symbol = "X"

    print_board(board)
    next_move(board,symbol)
    print_board(board)

    while not there_is_tie() and not there_is_win():
        if symbol == 'X':
            symbol = 'O'
        else:
            symbol = 'X'

        next_move(board,symbol)
        print_board(board)


