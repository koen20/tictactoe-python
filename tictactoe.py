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


def show_board():
    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()


# Get all cells that are empty
def get_empty_fields():
    empty_fields = []
    for x, row in enumerate(board):
        for y, cell in enumerate(row):
            if cell == '-':
                empty_fields.append([x, y])

    return empty_fields


def action_possible(row, cell):
    return board[row][cell] == '-'


def user_input(player):
    print("Voer het veld in waar je een X wilt invullen (rij,kolom). Bijv. '1,3'")
    inp = input()
    inp_split = inp.split(',')
    x = int(inp_split[0]) - 1
    y = int(inp_split[1]) - 1
    if action_possible(x, y):
        board[x][y] = player
    else:
        print("Invalid input")
        user_input(player)


def game():
    player = 'O' if random.randint(0, 1) == 0 else 'X'
    while not (check_win('X') or check_win('O') or len(get_empty_fields()) == 0):
        show_board()
        if player == "X":
            print('Human')
            user_input('X')
            player = "O"
        else:
            print('Computer turn')
            user_input("O")
            player = "X"

        # clear the console, linux: 'clear' windows: 'cls'
        os.system('cls' if os.name == 'nt' else 'clear')

    show_board()


if __name__ == '__main__':
    game()

