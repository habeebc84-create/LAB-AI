"""Decision Tree (CO4)

Train a Decision Tree classifier on the Iris dataset.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score


def main():
    data = load_iris()
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(X_train, y_train)
    pred = clf.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, pred))
    print(export_text(clf, feature_names=list(data.feature_names)))


if __name__ == "__main__":
    main()
