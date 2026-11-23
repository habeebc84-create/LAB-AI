"""Map Colouring (Constraint Satisfaction Problem) (CO5)

Color a map (Australia regions) with k colors.
"""

REGIONS = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
NEIGHBORS = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["Q", "SA", "V"],
    "V": ["SA", "NSW"],
    "T": [],
}


def solve_coloring(colors, assignment=None):
    if assignment is None:
        assignment = {}
    if len(assignment) == len(REGIONS):
        return dict(assignment)
    unassigned = [r for r in REGIONS if r not in assignment]
    region = unassigned[0]
    for color in colors:
        if all(assignment.get(nb) != color for nb in NEIGHBORS[region]):
            assignment[region] = color
            result = solve_coloring(colors, assignment)
            if result is not None:
                return result
            del assignment[region]
    return None


if __name__ == "__main__":
    colors = ["Red", "Green", "Blue"]
    sol = solve_coloring(colors)
    if sol is None:
        print("No solution with", len(colors), "colors")
    else:
        print("Coloring:")
        for r in REGIONS:
            print(f"  {r}: {sol[r]}")
