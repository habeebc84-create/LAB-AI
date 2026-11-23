"""Feed Forward Neural Network (CO4)

A feed-forward neural network (MLP) on Iris.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler


def main():
    data = load_iris()
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    mlp = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=1000, random_state=42)
    mlp.fit(X_train, y_train)
    pred = mlp.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, pred))
    print("Loss curve last:", mlp.loss_curve_[-1])


if __name__ == "__main__":
    main()
