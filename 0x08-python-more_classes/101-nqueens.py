#!/usr/bin/python3
import sys


def nqueens(N):
    """
    Print every possible solution to the N queens problem.

    Args:
        N (int): The size of the chessboard and the number of queens to place.

    Raises:
        TypeError: If N is not an integer.
        ValueError: If N is less than 4.

    Returns:
        None
    """
    # if not isinstance(N, int):
    #     raise TypeError("N must be a number")
    # if N < 4:
    #     raise ValueError("N must be at least 4")

    def is_valid(board, row, col):
        """
        Check if queen can be placed at given position

        Args:
            board (List[int]): The current state of the board.
            row (int): The row to check.
            col (int): The column to check.

        Returns:
            bool: True if the position is valid, False otherwise.
        """
        for r, c in enumerate(board):
            if c == col or abs(col - c) == abs(row - r) and r < row:
                return False
        return True

    def dfs(board, row):
        """
        Perform a depth-first search of the possible solutions

        Args:
            board (List[int]): The current state of the board.
            row (int): The starting row to search.

        Returns:
            None
        """
        if row == N:
            ans = []
            for r, c in enumerate(board):
                ans.append([r, c])
            print(ans)
            return

        for col in range(N):
            if is_valid(board, row, col):
                board[row] = col
                dfs(board, row + 1)
                board[row] = -1

    dfs([-1] * N, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    nqueens(N)
