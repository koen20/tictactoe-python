import os
import random

board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]


def check_win(player):
    win_board = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]

    if [player, player, player] in win_board:
        return True
    else:
        return False


def show_board(board_i):
    for row in board_i:
        for cell in row:
            print(cell, end=' ')
        print()


# Get all cells that are empty
def get_empty_fields(board_i):
    empty_fields = []
    for x, row in enumerate(board_i):
        for y, cell in enumerate(row):
            if cell == '-':
                empty_fields.append([x, y])

    return empty_fields


def action_possible(row, cell):
    return board[row][cell] == '-'


def user_input(player):
    print("_____")
    show_board([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    print("Voer het getal van het veld in waar je een " + player + " wilt invullen")
    options = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }
    while True:
        try:
            inp = input()
            cell = options[int(inp)]
            if action_possible(cell[0], cell[1]):
                board[cell[0]][cell[1]] = player
                break
            else:
                print("Het veld is al ingevuld")
        except (KeyError, ValueError):
            print("Onjuiste invoer")


def get_best_action(board_i, player):
    best_move = [0, 0]
    best_score = -100

    if len(get_empty_fields(board)) == 9:
        return [random.randint(0, 2), random.randint(0, 2)]

    for move in get_empty_fields(board_i):
        board_i[move[0]][move[1]] = player
        move_score = minimax(board_i, player, False, 0)
        board_i[move[0]][move[1]] = '-'
        if move_score > best_score:
            best_score = move_score
            best_move = move

    return best_move


def minimax(board_i, player, maximize, depth):
    opponent = 'O' if player == 'X' else 'X'
    if check_win(player):
        return 10 - depth

    if check_win(opponent):
        return -10 + depth

    if len(get_empty_fields(board_i)) == 0:
        return 0

    if maximize:
        best = -100
        for move in get_empty_fields(board_i):
            board_i[move[0]][move[1]] = player
            best = max(best, minimax(board_i, player, not maximize, depth + 1))
            board_i[move[0]][move[1]] = '-'

        return best
    else:
        best = 100
        for move in get_empty_fields(board_i):
            board_i[move[0]][move[1]] = opponent
            best = min(best, minimax(board_i, player, not maximize, depth + 1))
            board_i[move[0]][move[1]] = '-'

        return best


def game():
    player = 'O' if random.randint(0, 1) == 0 else 'X'
    while True:
        if check_win('X'):
            print('Speler X heeft gewonnen')
            break
        elif check_win('O'):
            print('Speler O heeft gewonnen')
            break
        elif len(get_empty_fields(board)) == 0:
            print("Gelijkspel")
            break

        show_board(board)
        if player == "X":
            user_input('X')
            player = "O"
        else:
            print('Computer')
            action = get_best_action(board, player)
            board[action[0]][action[1]] = 'O'
            player = "X"

        # clear the console, linux: 'clear' windows: 'cls'
        os.system('cls' if os.name == 'nt' else 'clear')

    show_board(board)


if __name__ == '__main__':
    game()
