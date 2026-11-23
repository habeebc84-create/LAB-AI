"""Reinforcement Learning Agent (Q-Learning) (CO2)

Q-learning on a 5x5 grid.
"""

import random
import numpy as np

random.seed(42)
np.random.seed(42)

ROWS, COLS = 5, 5
ACTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
GOAL = (4, 4)
alpha = 0.1
gamma = 0.9
epsilon = 0.2
episodes = 500
Q = np.zeros((ROWS, COLS, len(ACTIONS)))


def step(state, action_idx):
    r, c = state
    dr, dc = ACTIONS[action_idx]
    nr, nc = r + dr, c + dc
    if 0 <= nr < ROWS and 0 <= nc < COLS:
        state = (nr, nc)
    reward = 10 if state == GOAL else -0.1
    done = state == GOAL
    return state, reward, done


for ep in range(episodes):
    state = (0, 0)
    for _ in range(100):
        if random.random() < epsilon:
            a = random.randrange(len(ACTIONS))
        else:
            a = int(np.argmax(Q[state[0], state[1]]))
        ns, r, done = step(state, a)
        Q[state[0], state[1], a] += alpha * (r + gamma * np.max(Q[ns[0], ns[1]]) - Q[state[0], state[1], a])
        state = ns
        if done:
            break

state = (0, 0)
path = [state]
for _ in range(50):
    a = int(np.argmax(Q[state[0], state[1]]))
    ns, r, done = step(state, a)
    path.append(ns)
    state = ns
    if done:
        break
print("Learned path:", path)
