"""Support Vector Machine (SVM) for Binary Classification (CO4)

SVM classifier on a binary Iris subset.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

data = load_iris()
X = data.data
y = (data.target != 0).astype(int)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
for kernel in ("linear", "rbf", "poly"):
    svm = SVC(kernel=kernel)
    svm.fit(X_train, y_train)
    pred = svm.predict(X_test)
    print(f"kernel={kernel} accuracy={accuracy_score(y_test, pred):.3f}")
svm = SVC(kernel="rbf")
svm.fit(X_train, y_train)
pred = svm.predict(X_test)
print(classification_report(y_test, pred))
