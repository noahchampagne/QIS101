#!/usr/bin/env python3
"""connect_four.py"""


def print_winner(board: list[list[int]]) -> int:
    """Takes in a 2d list resembling a Connect 4 board and prints who won"""

    def track(r: int, c: int, dir: tuple[int, int], count: int) -> bool:
        """Takes in a position on the board and recursively tracks whether it is a
        winning position through directional tracking and counting"""
        # Base case which returns false if out of bounds or if the streak stopped
        if r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != player:
            return False
        elif count == 4:
            return True
        # If the possibility to winning remains, recurses to the next position
        return track(r + dir[0], c + dir[1], dir, count + 1)

    directions: list[tuple[int, int]] = [(1, 0), (1, 1), (0, 1), (1, -1)]
    # Loops through all the board positions minus the one's where a streak can't start
    for row in range(len(board) - 3):
        for col in range(len(board[0]) - 3):
            if player := board[row][col]:
                for dir in directions:
                    if track(row, col, dir, 1):
                        print(player)
                        return player
    print("No winner :(")
    return 0


def main() -> None:
    board1: list[list[int]] = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 2, 2, 1, 1, 0, 0],
        [0, 2, 1, 2, 2, 0, 1],
        [2, 1, 1, 1, 2, 0, 2],
    ]
    print_winner(board1)
    board2: list[list[int]] = [
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 2, 2, 2, 2, 1, 0],
        [0, 1, 1, 2, 2, 2, 0],
        [2, 2, 1, 1, 1, 2, 0],
    ]
    print_winner(board2)

    board3: list[list[int]] = [
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
