"""Genetic Algorithm to Evolve a Neural Network (CO1)

Evolve NN weights for XOR using GA.
"""

import random
import numpy as np

random.seed(42)
np.random.seed(42)

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
y = np.array([0, 1, 1, 0], dtype=float)
N_WEIGHTS = 9


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def forward(w, x):
    w = np.array(w)
    W1 = w[0:4].reshape(2, 2)
    b1 = w[4:6]
    W2 = w[6:8].reshape(2, 1)
    b2 = w[8]
    h = sigmoid(x @ W1 + b1)
    out = sigmoid(h @ W2 + b2)
    return out


def fitness(w):
    preds = np.array([forward(w, xi)[0] for xi in X])
    labels = (preds > 0.5).astype(int)
    acc = np.mean(labels == y)
    mse = np.mean((preds - y) ** 2)
    return acc - mse

POP = 60
GENS = 200
MUT = 0.1


def main():
    pop = [np.random.uniform(-2, 2, N_WEIGHTS) for _ in range(POP)]
    for gen in range(GENS):
        scored = sorted(pop, key=fitness, reverse=True)
        parents = scored[:POP // 4]
        new_pop = list(parents)
        while len(new_pop) < POP:
            a, b = random.sample(parents, 2)
            point = random.randint(1, N_WEIGHTS - 1)
            child = np.concatenate([a[:point], b[point:]])
            if random.random() < MUT:
                idx = random.randrange(N_WEIGHTS)
                child[idx] += random.gauss(0, 0.5)
            new_pop.append(child)
        pop = new_pop
    best = max(pop, key=fitness)
    print("Best fitness:", fitness(best))
    for xi in X:
        print(xi, "->", round(float(forward(best, xi)[0]), 3))


if __name__ == "__main__":
    main()
