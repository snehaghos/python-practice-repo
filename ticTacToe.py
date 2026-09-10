# Tic Tac Toe - 2 Player Game
# Simple and easy to understand

def print_board(board):
    print()
    print("  " + board[0] + " | " + board[1] + " | " + board[2])
    print(" ---+---+---")
    print("  " + board[3] + " | " + board[4] + " | " + board[5])
    print(" ---+---+---")
    print("  " + board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(board, player):
    # All possible winning lines
    win_lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for line in win_lines:
        if board[line[0]] == board[line[1]] == board[line[2]] == player:
            return True
    return False

def is_full(board):
    return " " not in board

def tic_tac_toe():
    board = [" " for _ in range(9)]
    current_player = "X"

    print("=== TIC TAC TOE ===")
    print("Player 1 = X | Player 2 = O")
    print("Enter position 1-9:")
    print("  1 | 2 | 3")
    print(" ---+---+---")
    print("  4 | 5 | 6")
    print(" ---+---+---")
    print("  7 | 8 | 9")

    while True:
        print_board(board)

        # Get player move
        while True:
            try:
                pos = int(input(f"Player {current_player}, enter position (1-9): "))
                if pos < 1 or pos > 9:
                    print("Enter a number between 1 and 9!")
                    continue
                if board[pos - 1] != " ":
                    print("That spot is taken! Try again.")
                    continue
                break
            except ValueError:
                print("Enter a valid number!")

        # Make the move
        board[pos - 1] = current_player

        # Check if current player won
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins! Congratulations!")
            break

        # Check if board is full (tie)
        if is_full(board):
            print_board(board)
            print("It's a tie! Good game!")
            break

        # Switch player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

if __name__ == "__main__":
    tic_tac_toe()
    play_again = input("\nPlay again? (y/n): ")
    if play_again.lower() == "y":
        tic_tac_toe()
