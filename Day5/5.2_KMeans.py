"""K-Means Clustering (CO2)

K-Means clustering on Iris.
"""

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, silhouette_score
from sklearn.preprocessing import StandardScaler

data = load_iris()
X = StandardScaler().fit_transform(data.data)
for k in (2, 3, 4, 5):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = km.fit_predict(X)
    print(f"k={k} inertia={km.inertia_:.2f} silhouette={silhouette_score(X, labels):.3f}")
km = KMeans(n_clusters=3, random_state=42, n_init=10)
labels = km.fit_predict(X)
print("Adjusted Rand Index vs true labels:", adjusted_rand_score(data.target, labels))
