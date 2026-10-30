from app import (
    create_board,
    check_winner,
    is_draw,
    make_move
)


def test_create_board():
    board = create_board()
    assert len(board) == 9


def test_valid_move():
    board = create_board()
    assert make_move(board, 0, "X")
    assert board[0] == "X"


def test_invalid_move():
    board = create_board()
    assert make_move(board, 0, "X")
    assert not make_move(board, 0, "O")


def test_winner():
    board = ["X", "X", "X",
             "O", "O", " ",
             " ", " ", " "]

    assert check_winner(board) == "X"


def test_draw():
    board = [
        "X", "O", "X",
        "X", "O", "O",
        "O", "X", "X"
    ]

    assert is_draw(board)


def test_no_winner():
    board = create_board()
    assert check_winner(board) is None