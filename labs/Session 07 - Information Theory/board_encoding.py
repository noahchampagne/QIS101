#!/usr/bin/env python3
"""board_encoding.py"""


def decrypt(board: int) -> None:
    """Decrypt's a Tic-Tac-Toe board that has been encoded using a single number"""
    squares: list[int] = []
    # Gets the square values from the inputted number
    for _ in range(9):
        num: int = board % 3
        squares.append("X" if num == 1 else "0" if num == 2 else " ")  # type: ignore
        board //= 3
    # Prints the Tic-Tac-Toe board
    for i in range(3):
        print(f" {squares[3*i]} | {squares[3*i + 1]} | {squares[3*i + 2]}")
        if i != 2:
            print("--- " * 3)
    print("")


def main() -> None:
    board_1: int = 2271
    board_2: int = 1638
    board_3: int = 12065
    decrypt(board_1)
    decrypt(board_2)
    decrypt(board_3)


if __name__ == "__main__":
    main()
