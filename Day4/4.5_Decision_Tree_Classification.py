"""Decision Tree for a Simple Classification Problem (CO3)

Decision tree on a small synthetic weather dataset.
"""

from sklearn.tree import DecisionTreeClassifier, export_text
import pandas as pd

data = {
    "Outlook": ["Sunny", "Sunny", "Overcast", "Rain", "Rain", "Rain", "Overcast", "Sunny"],
    "Temp": ["Hot", "Hot", "Hot", "Mild", "Cool", "Cool", "Cool", "Mild"],
    "Humidity": ["High", "High", "High", "High", "Normal", "Normal", "Normal", "High"],
    "Wind": ["Weak", "Strong", "Weak", "Weak", "Weak", "Strong", "Strong", "Weak"],
    "Play": ["No", "No", "Yes", "Yes", "Yes", "No", "Yes", "No"],
}
df = pd.DataFrame(data)
X = pd.get_dummies(df.drop("Play", axis=1))
y = df["Play"]
clf = DecisionTreeClassifier(criterion="entropy", random_state=42)
clf.fit(X, y)
print("Accuracy on training:", clf.score(X, y))
print(export_text(clf, feature_names=list(X.columns)))
