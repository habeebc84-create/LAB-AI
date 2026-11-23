"""Sentiment Analysis using NLP (CO3)

Simple sentiment classifier using TF-IDF and Logistic Regression.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

texts = [
    "I love this movie, it is great",
    "This film was amazing and wonderful",
    "What a fantastic experience",
    "I really enjoyed this",
    "Absolutely brilliant",
    "I hate this movie, it is terrible",
    "This film was awful and boring",
    "What a horrible experience",
    "I really disliked this",
    "Absolutely dreadful",
]
labels = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.3, random_state=42)
vec = TfidfVectorizer()
Xtr = vec.fit_transform(X_train)
Xte = vec.transform(X_test)
clf = LogisticRegression()
clf.fit(Xtr, y_train)
pred = clf.predict(Xte)
print("Accuracy:", accuracy_score(y_test, pred))
print(classification_report(y_test, pred))
sample = ["I love it", "I hate it"]
print("Demo:", clf.predict(vec.transform(sample)))
