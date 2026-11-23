"""Alpha-Beta Pruning Algorithm for Gaming (CO3)

Minimax with alpha-beta pruning on the take-away game.
"""

nodes = 0


def alphabeta(stones, is_max, alpha, beta):
    global nodes
    nodes += 1
    if stones == 0:
        return -1 if is_max else 1
    if is_max:
        best = -float("inf")
        for move in (1, 2, 3):
            if move <= stones:
                val = alphabeta(stones - move, False, alpha, beta)
                best = max(best, val)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
        return best
    else:
        best = float("inf")
        for move in (1, 2, 3):
            if move <= stones:
                val = alphabeta(stones - move, True, alpha, beta)
                best = min(best, val)
                beta = min(beta, best)
                if beta <= alpha:
                    break
        return best


def best_move(stones):
    global nodes
    nodes = 0
    best_val = -float("inf")
    move = 1
    alpha, beta = -float("inf"), float("inf")
    for m in (1, 2, 3):
        if m <= stones:
            val = alphabeta(stones - m, False, alpha, beta)
            if val > best_val:
                best_val = val
                move = m
            alpha = max(alpha, best_val)
    return move, best_val, nodes


if __name__ == "__main__":
    for n in [5, 10, 15]:
        m, v, nd = best_move(n)
        print(f"stones={n}: best move={m} value={v} nodes={nd}")
