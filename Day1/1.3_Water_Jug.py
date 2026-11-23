"""Water Jug Problem (CO2)

Measure exactly target gallons using two jugs of capacities (cap1, cap2).
Uses BFS over (a, b) states.
"""

from collections import deque


def solve(cap1, cap2, target):
    start = (0, 0)
    if target > max(cap1, cap2):
        return None
    visited = {start}
    q = deque([(start, [start])])
    while q:
        (a, b), path = q.popleft()
        if a == target or b == target:
            return path
        next_states = []
        next_states.append((cap1, b))
        next_states.append((a, cap2))
        next_states.append((0, b))
        next_states.append((a, 0))
        pour = min(a, cap2 - b)
        next_states.append((a - pour, b + pour))
        pour = min(b, cap1 - a)
        next_states.append((a + pour, b - pour))
        for ns in next_states:
            if ns not in visited:
                visited.add(ns)
                q.append((ns, path + [ns]))
    return None


if __name__ == "__main__":
    path = solve(4, 3, 2)
    if path is None:
        print("No solution")
    else:
        print("Steps (jug1, jug2):")
        for s in path:
            print(s)
