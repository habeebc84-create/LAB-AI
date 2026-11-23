"""Bayesian Network for Probabilistic Relationships (CO4)

Small Bayesian network with inference by enumeration.
"""

P_R = {True: 0.2, False: 0.8}
P_S_given_R = {True: {True: 0.01, False: 0.99}, False: {True: 0.4, False: 0.6}}
P_W_given_RS = {
    (True, True): {True: 0.99, False: 0.01},
    (True, False): {True: 0.8, False: 0.2},
    (False, True): {True: 0.9, False: 0.1},
    (False, False): {True: 0.0, False: 1.0},
}


def joint(r, s, w):
    return P_R[r] * P_S_given_R[r][s] * P_W_given_RS[(r, s)][w]


def query(target_var, evidence):
    total = 0.0
    dist = {}
    for r in (True, False):
        for s in (True, False):
            for w in (True, False):
                vals = {"R": r, "S": s, "W": w}
                ok = all(vals[k] == v for k, v in evidence.items())
                if not ok:
                    continue
                j = joint(r, s, w)
                key = vals[target_var]
                dist[key] = dist.get(key, 0) + j
                total += j
    for k in dist:
        dist[k] /= total
    return dist


if __name__ == "__main__":
    print("P(Rain | WetGrass=True):", query("R", {"W": True}))
    print("P(Sprinkler | WetGrass=True):", query("S", {"W": True}))
