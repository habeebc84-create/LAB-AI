"""Missionaries and Cannibals Problem (CO3)

Move 3 missionaries and 3 cannibals across a river. Boat holds 1 or 2.
Never leave missionaries outnumbered by cannibals on either bank.
BFS over states (m_left, c_left, boat).
"""

from collections import deque


def valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m > 0 and c > m:
        return False
    mr, cr = 3 - m, 3 - c
    if mr > 0 and cr > mr:
        return False
    return True


def moves():
    res = []
    for dm in range(0, 3):
        for dc in range(0, 3):
            if 1 <= dm + dc <= 2:
                res.append((dm, dc))
    return res


def solve():
    start = (3, 3, 0)
    goal = (0, 0, 1)
    visited = {start}
    q = deque([(start, [start])])
    while q:
        (m, c, boat), path = q.popleft()
        if (m, c, boat) == goal:
            return path
        for dm, dc in moves():
            if boat == 0:
                nm, nc, nb = m - dm, c - dc, 1
            else:
                nm, nc, nb = m + dm, c + dc, 0
            if valid(nm, nc):
                ns = (nm, nc, nb)
                if ns not in visited:
                    visited.add(ns)
                    q.append((ns, path + [ns]))
    return None


if __name__ == "__main__":
    path = solve()
    if path is None:
        print("No solution")
    else:
        print(f"Solution in {len(path)-1} crossings:")
        for s in path:
            print(s)
