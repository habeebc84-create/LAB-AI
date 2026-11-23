"""8-Puzzle Problem (CO1)

Solve the classic 8-puzzle using A* search with the Manhattan distance
heuristic. State is a 3x3 tuple; 0 represents the blank tile.
"""

import heapq

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)


def manhattan(state):
    dist = 0
    for idx, tile in enumerate(state):
        if tile == 0:
            continue
        goal_idx = tile - 1
        r1, c1 = divmod(idx, 3)
        r2, c2 = divmod(goal_idx, 3)
        dist += abs(r1 - r2) + abs(c1 - c2)
    return dist


def neighbors(state):
    i = state.index(0)
    r, c = divmod(i, 3)
    moves = []
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            j = nr * 3 + nc
            lst = list(state)
            lst[i], lst[j] = lst[j], lst[i]
            moves.append(tuple(lst))
    return moves


def solve(start):
    if start == GOAL:
        return [start]
    open_heap = [(manhattan(start), 0, start)]
    came_from = {start: None}
    g_score = {start: 0}
    closed = set()
    while open_heap:
        _, g, current = heapq.heappop(open_heap)
        if current in closed:
            continue
        closed.add(current)
        if current == GOAL:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path
        for nb in neighbors(current):
            tentative = g + 1
            if nb in closed:
                continue
            if tentative < g_score.get(nb, float("inf")):
                came_from[nb] = current
                g_score[nb] = tentative
                f = tentative + manhattan(nb)
                heapq.heappush(open_heap, (f, tentative, nb))
    return None


def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i + 3])
    print()


if __name__ == "__main__":
    start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
    path = solve(start)
    if path is None:
        print("No solution")
    else:
        print(f"Solution in {len(path) - 1} moves:")
        for s in path:
            print_state(s)
