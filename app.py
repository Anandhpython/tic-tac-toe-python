WINNING_COMBINATIONS = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]


def create_board():
    return [" "] * 9


def check_winner(board):
    for a, b, c in WINNING_COMBINATIONS:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    return None


def is_draw(board):
    return " " not in board and check_winner(board) is None


def make_move(board, position, player):
    if position < 0 or position > 8:
        return False

    if board[position] != " ":
        return False

    if player not in ("X", "O"):
        return False

    board[position] = player
    return True


def display_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i + 3]))
        if i < 6:
            print("--+---+--")


def play_game():
    board = create_board()
    current_player = "X"

    while True:
        display_board(board)

        try:
            position = int(input(
                f"Player {current_player}, enter position (1-9): "
            )) - 1
        except ValueError:
            print("Please enter a valid number.")
            continue

        if not make_move(board, position, current_player):
            print("Invalid move. Try again.")
            continue

        winner = check_winner(board)

        if winner:
            display_board(board)
            print(f"Player {winner} wins!")
            break

        if is_draw(board):
            display_board(board)
            print("Game is a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play_game()