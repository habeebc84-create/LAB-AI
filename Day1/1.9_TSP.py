"""Travelling Salesman Problem (CO4)

Find the shortest route visiting all cities once and returning to start.
"""

from itertools import permutations


def tsp(dist):
    n = len(dist)
    cities = list(range(1, n))
    best = None
    best_route = None
    for perm in permutations(cities):
        route = [0] + list(perm) + [0]
        cost = sum(dist[route[i]][route[i + 1]] for i in range(len(route) - 1))
        if best is None or cost < best:
            best = cost
            best_route = route
    return best, best_route


if __name__ == "__main__":
    dist = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0],
    ]
    cost, route = tsp(dist)
    print("Best cost:", cost)
    print("Route:", route)
