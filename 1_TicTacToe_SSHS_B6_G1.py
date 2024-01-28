board = [' '] * 9

def print_board():
    print('---------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('---------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('---------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('---------')

def check_win(player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
       (board[3] == player and board[4] == player and board[5] == player) or \
       (board[6] == player and board[7] == player and board[8] == player) or \
       (board[0] == player and board[3] == player and board[6] == player) or \
       (board[1] == player and board[4] == player and board[7] == player) or \
       (board[2] == player and board[5] == player and board[8] == player) or \
       (board[0] == player and board[4] == player and board[8] == player) or \
       (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False

def check_full():
    return ' ' not in board

current_player = 'X'
while True:
    print_board()

    while True:
        move = input("Enter your move (0-8): ")
        if move.isdigit() and int(move) in range(9) and board[int(move)] == ' ':
            move = int(move)
            break
        else:
            print("Invalid move. Try again!")

    board[move] = current_player

    if check_win(current_player):
        print_board()
        print("Player", current_player, "wins!")
        break

    if check_full():
        print_board()
        print("It's a tie!")
        break

    current_player = 'O' if current_player == 'X' else 'X'