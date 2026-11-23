"""Breadth First Search (BFS) (CO3)

Generic BFS on an unweighted graph.
"""

from collections import deque


def bfs(graph, start, goal):
    if start == goal:
        return [start]
    visited = {start}
    q = deque([(start, [start])])
    while q:
        node, path = q.popleft()
        for nb in graph.get(node, []):
            if nb == goal:
                return path + [nb]
            if nb not in visited:
                visited.add(nb)
                q.append((nb, path + [nb]))
    return None


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": [],
    }
    print("BFS path A->F:", bfs(graph, "A", "F"))
