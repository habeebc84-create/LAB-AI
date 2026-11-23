"""Linear Regression (CO4)

Simple linear regression on a synthetic dataset.
"""

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


def main():
    rng = np.random.RandomState(42)
    X = 2 * rng.rand(100, 1)
    y = 4 + 3 * X[:, 0] + rng.randn(100)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print("Coefficients:", model.coef_, "Intercept:", model.intercept_)
    print("MSE:", mean_squared_error(y_test, pred))
    print("R2:", r2_score(y_test, pred))


if __name__ == "__main__":
    main()
