"""Recommendation System using Collaborative Filtering (CO5)

User-based collaborative filtering.
"""

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

ratings = np.array([
    [5, 3, 0, 1],
    [4, 0, 0, 1],
    [1, 1, 0, 5],
    [1, 0, 0, 4],
    [0, 1, 5, 4],
], dtype=float)

sim = cosine_similarity(ratings)
np.fill_diagonal(sim, 0)

def recommend(user_idx, k=2, n=2):
    sims = sim[user_idx]
    top = np.argsort(sims)[::-1][:k]
    scores = np.zeros(ratings.shape[1])
    for u in top:
        scores += sims[u] * ratings[u]
    rated = ratings[user_idx] > 0
    scores[rated] = -1
    recs = np.argsort(scores)[::-1][:n]
    return recs, scores[recs]

if __name__ == "__main__":
    for u in range(len(ratings)):
        recs, sc = recommend(u)
        print(f"User {u}: recommend items {list(recs)} (scores {sc})")
