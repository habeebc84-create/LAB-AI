"""8-Queen Problem (CO1)

Place 8 queens on an 8x8 chessboard so that no two attack each other.
Uses backtracking.
"""

N = 8


def is_safe(board, row, col):
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve_n_queens(n=N):
    board = [-1] * n
    solutions = []

    def backtrack(row):
        if row == n:
            solutions.append(list(board))
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)
    return solutions


def print_board(board):
    for r in range(len(board)):
        line = ["Q" if c == board[r] else "." for c in range(len(board))]
        print(" ".join(line))
    print()


if __name__ == "__main__":
    sols = solve_n_queens()
    print(f"Found {len(sols)} solutions")
    print("First solution:")
    print_board(sols[0])
