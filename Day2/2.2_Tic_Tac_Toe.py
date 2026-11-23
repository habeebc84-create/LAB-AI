"""Tic Tac Toe Game (CO3)

Console Tic-Tac-Toe with an unbeatable AI using minimax.
"""

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
]


def check_winner(board):
    for a, b, c in WIN_LINES:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    if " " not in board:
        return "Draw"
    return None


def minimax(board, is_max, ai="O", human="X"):
    res = check_winner(board)
    if res == ai:
        return 1
    if res == human:
        return -1
    if res == "Draw":
        return 0
    if is_max:
        best = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = ai
                best = max(best, minimax(board, False, ai, human))
                board[i] = " "
        return best
    else:
        best = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = human
                best = min(best, minimax(board, True, ai, human))
                board[i] = " "
        return best


def best_move(board, ai="O", human="X"):
    best_val = -float("inf")
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = ai
            val = minimax(board, False, ai, human)
            board[i] = " "
            if val > best_val:
                best_val = val
                move = i
    return move


def print_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i + 3]))
        if i < 6:
            print("-" * 9)


if __name__ == "__main__":
    board = [" "] * 9
    turn = "X"
    while check_winner(board) is None:
        if turn == "X":
            m = None
            for i in range(9):
                if board[i] == " ":
                    m = i
                    break
            if m is None:
                break
            board[m] = "X"
            turn = "O"
        else:
            m = best_move(board)
            board[m] = "O"
            turn = "X"
    print_board(board)
    print("Result:", check_winner(board))
