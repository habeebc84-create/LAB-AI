"""A* Algorithm (CO4)

Generic A* search on a weighted graph with a heuristic function.
"""

import heapq


def a_star(graph, heuristic, start, goal):
    open_heap = [(heuristic(start), 0, start)]
    came_from = {start: None}
    g_score = {start: 0}
    closed = set()
    while open_heap:
        _, g, current = heapq.heappop(open_heap)
        if current in closed:
            continue
        closed.add(current)
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path, g_score[goal]
        for nb, cost in graph.get(current, []):
            tentative = g + cost
            if nb in closed:
                continue
            if tentative < g_score.get(nb, float("inf")):
                came_from[nb] = current
                g_score[nb] = tentative
                f = tentative + heuristic(nb)
                heapq.heappush(open_heap, (f, tentative, nb))
    return None, float("inf")


if __name__ == "__main__":
    graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("C", 2), ("D", 5)],
        "C": [("D", 1)],
        "D": [],
    }
    h = {"A": 7, "B": 6, "C": 2, "D": 0}
    path, cost = a_star(graph, lambda n: h[n], "A", "D")
    print("A* path:", path, "cost:", cost)
