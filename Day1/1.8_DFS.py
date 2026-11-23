"""Depth First Search (DFS) (CO4)

Generic DFS on a graph.
"""

def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    if start == goal:
        return [start]
    for nb in graph.get(start, []):
        if nb not in visited:
            path = dfs(graph, nb, goal, visited)
            if path is not None:
                return [start] + path
    return None


def dfs_traversal(graph, start):
    visited = set()
    order = []

    def rec(node):
        visited.add(node)
        order.append(node)
        for nb in graph.get(node, []):
            if nb not in visited:
                rec(nb)

    rec(start)
    return order


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": [],
    }
    print("DFS path A->F:", dfs(graph, "A", "F"))
    print("DFS traversal from A:", dfs_traversal(graph, "A"))
