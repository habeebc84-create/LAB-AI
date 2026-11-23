"""Genetic Algorithm for Optimising a Function (CO4)

Maximize f(x) = x * sin(10*pi*x) + 1.0 on [-1, 2].
"""

import random
import math

random.seed(42)

def fitness(x):
    return x * math.sin(10 * math.pi * x) + 1.0

def decode(gene):
    return gene / 65535 * 3 - 1

POP = 50
GENS = 50
MUT = 0.05

def main():
    pop = [random.randint(0, 65535) for _ in range(POP)]
    for gen in range(GENS):
        scored = sorted(pop, key=lambda g: fitness(decode(g)), reverse=True)
        parents = scored[:POP // 2]
        new_pop = list(parents)
        while len(new_pop) < POP:
            a, b = random.sample(parents, 2)
            point = random.randint(1, 15)
            mask = (1 << point) - 1
            child = (a & mask) | (b & ~mask)
            if random.random() < MUT:
                child ^= 1 << random.randint(0, 15)
            new_pop.append(child)
        pop = new_pop
    best = max(pop, key=lambda g: fitness(decode(g)))
    print("Best x:", decode(best), "f(x):", fitness(decode(best)))

if __name__ == "__main__":
    main()
