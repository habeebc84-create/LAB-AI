"""Minimax Algorithm for Gaming (CO3)

Demonstrates minimax on a take-away game.
"""

def minimax(stones, is_max):
    if stones == 0:
        return -1 if is_max else 1
    if is_max:
        best = -float("inf")
        for move in (1, 2, 3):
            if move <= stones:
                best = max(best, minimax(stones - move, False))
        return best
    else:
        best = float("inf")
        for move in (1, 2, 3):
            if move <= stones:
                best = min(best, minimax(stones - move, True))
        return best


def best_move(stones):
    best_val = -float("inf")
    move = 1
    for m in (1, 2, 3):
        if m <= stones:
            val = minimax(stones - m, False)
            if val > best_val:
                best_val = val
                move = m
    return move, best_val


if __name__ == "__main__":
    for n in range(1, 15):
        m, v = best_move(n)
        print(f"stones={n}: best move={m} (value={v})")
