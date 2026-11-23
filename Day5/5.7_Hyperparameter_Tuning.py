"""Hyper-parameter Tuning for a Machine Learning Model (CO4)

Grid search over RandomForest hyperparameters.
"""

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import accuracy_score

data = load_iris()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
param_grid = {
    "n_estimators": [50, 100],
    "max_depth": [None, 3, 5],
    "min_samples_split": [2, 4],
}
grid = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=5, n_jobs=-1)
grid.fit(X_train, y_train)
print("Best params:", grid.best_params_)
print("Best CV score:", grid.best_score_)
pred = grid.predict(X_test)
print("Test accuracy:", accuracy_score(y_test, pred))
