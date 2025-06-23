#!/usr/bin/env python3
"""connect_four.py"""

def check_winner(player: int, board: list[list[int]]) -> bool:
    """Return True if *player* (1 or 2) has four in-a-row on *board*."""
    rows, cols = len(board), len(board[0])

    for r in range(rows):
        for c in range(cols):
            if board[r][c] != player:
                continue

            # ── horizontal →
            if c + 3 < cols and all(board[r][c + k] == player for k in range(4)):
                return True

            # │ vertical ↓
            if r + 3 < rows and all(board[r + k][c] == player for k in range(4)):
                return True

            # ╲ diagonal down-right
            if (
                r + 3 < rows
                and c + 3 < cols
                and all(board[r + k][c + k] == player for k in range(4))
            ):
                return True

            # ╱ diagonal down-left
            if (
                r + 3 < rows
                and c - 3 >= 0
                and all(board[r + k][c - k] == player for k in range(4))
            ):
                return True

    return False


def print_winner(board):
    print(*board, sep="\n")
    if check_winner(1, board):
        print("Player 1 wins!")
    elif check_winner(2, board):
        print("Player 2 wins!")
    else:
        print("No winner yet")
    print()


def main():
    board1 = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 2, 2, 1, 1, 0, 0],
        [0, 2, 1, 2, 2, 0, 1],
        [2, 1, 1, 1, 2, 0, 2],
    ]
    print_winner(board1)

    board2 = [
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 2, 2, 2, 2, 1, 0],
        [0, 1, 1, 2, 2, 2, 0],
        [2, 2, 1, 1, 1, 2, 0],
    ]
    print_winner(board2)

    board3 = [
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 2, 2, 0],
        [0, 1, 2, 1, 2, 2, 0],
        [0, 2, 2, 2, 1, 1, 0],
        [0, 1, 1, 2, 1, 2, 0],
    ]
    print_winner(board3)


if __name__ == "__main__":
    main()
