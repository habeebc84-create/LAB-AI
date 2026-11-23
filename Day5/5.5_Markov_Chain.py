"""Markov Chain Model for Predicting Sequences (CO3)

First-order Markov chain from text.
"""

import random
from collections import defaultdict, Counter

random.seed(42)

text = "the cat sat on the mat the cat ate the rat the dog chased the cat"
words = text.split()
transitions = defaultdict(Counter)
for a, b in zip(words, words[1:]):
    transitions[a][b] += 1
chain = {}
for w, counts in transitions.items():
    total = sum(counts.values())
    chain[w] = [(nxt, c / total) for nxt, c in counts.items()]


def next_word(w):
    if w not in chain:
        return None
    r = random.random()
    cum = 0.0
    for nxt, p in chain[w]:
        cum += p
        if r <= cum:
            return nxt
    return chain[w][-1][0]


def generate(start, length=10):
    seq = [start]
    for _ in range(length - 1):
        nw = next_word(seq[-1])
        if nw is None:
            break
        seq.append(nw)
    return seq

if __name__ == "__main__":
    print("Transitions:", dict(transitions))
    print("Generated:", " ".join(generate("the", 12)))
