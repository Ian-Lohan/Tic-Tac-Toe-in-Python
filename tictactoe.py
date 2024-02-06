import random


board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]


def print_board():
    for _ in range(3):
        print(board[_][0], "|", board[_][1], "|", board[_][2])
        if _ < 2:
            print("---------")


def validate_choice(choice):
    row = (choice - 1) // 3
    col = (choice - 1) % 3
    return board[row][col] != "X" and board[row][col] != "O"


def check_winner():
    for symbol in ["X", "O"]:
        if (board[0][0] == board[0][1] == board[0][2] == symbol or
            board[1][0] == board[1][1] == board[1][2] == symbol or
            board[2][0] == board[2][1] == board[2][2] == symbol or
            board[0][0] == board[1][0] == board[2][0] == symbol or
            board[0][1] == board[1][1] == board[2][1] == symbol or
            board[0][2] == board[1][2] == board[2][2] == symbol or
            board[0][0] == board[1][1] == board[2][2] == symbol or
            board[0][2] == board[1][1] == board[2][0] == symbol):
            return symbol
    return None

    
def computer_turn():
    row = random.choice(range(3))
    col = random.choice(range(3))
    while board[row][col] in ["X", "O"]:
        row = random.choice(range(3))
        col = random.choice(range(3))
    board[row][col] = "O"
    print_board()
    print()
    player_turn()


def player_turn():
    choice = int(input("Choose a position (1-9): "))
    while not validate_choice(choice):
            choice = int(input("Invalid. Choose a position (1-9): "))
    board[((choice - 1) // 3)][(choice - 1) % 3] = "X"
    print_board()
    print()
    winner = check_winner()
    if winner is not None:
        if winner == "X":
            print("Player wins!")
        else:
            print("Computer wins!")
        return
    computer_turn()


def main():
    print_board()
    player_turn()
    

main()