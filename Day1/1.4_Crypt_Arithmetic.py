"""Crypt-Arithmetic Problem (CO2)

Solve SEND + MORE = MONEY by assigning distinct digits to letters.
Generic backtracking solver for a single addition equation.
"""

from itertools import permutations


def solve_cryptarithm(words, result):
    letters = sorted(set("".join(words) + result))
    if len(letters) > 10:
        return None
    first_letters = {w[0] for w in words + [result]}
    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        if any(mapping[fl] == 0 for fl in first_letters):
            continue
        nums = [int("".join(str(mapping[ch]) for ch in w)) for w in words]
        res = int("".join(str(mapping[ch]) for ch in result))
        if sum(nums) == res:
            return mapping
    return None


def pretty(mapping, words, result):
    addends = ["".join(str(mapping[ch]) for ch in w) for w in words]
    res = "".join(str(mapping[ch]) for ch in result)
    return " + ".join(addends) + " = " + res


if __name__ == "__main__":
    mapping = solve_cryptarithm(["SEND", "MORE"], "MONEY")
    if mapping is None:
        print("No solution")
    else:
        print("Mapping:", mapping)
        print(pretty(mapping, ["SEND", "MORE"], "MONEY"))
