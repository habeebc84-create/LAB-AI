"""Dimensionality Reduction using PCA (CO4)

Apply PCA to Iris dataset.
"""

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np

data = load_iris()
X = StandardScaler().fit_transform(data.data)
pca = PCA(n_components=2)
X2 = pca.fit_transform(X)
print("Explained variance ratio:", pca.explained_variance_ratio_)
print("Total (2 comps):", pca.explained_variance_ratio_.sum())
print("Shape before:", X.shape, "after:", X2.shape)
pca_full = PCA()
pca_full.fit(X)
print("Cumulative variance:", np.cumsum(pca_full.explained_variance_ratio_))
