"""
# KNN

k nearest neighbours

Pro
- Relatively simple

Cons
- Computationally intensive
- Hard to represent relationships between features
"""
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# set up

iris = load_iris()

# f(X) = y
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5)

def accuracy_of(classifier):
    classifier.fit(X_train, y_train)

    predictions = classifier.predict(X_test)

    print(accuracy_score(y_test, predictions))

class KNN:
    def __init__(self):
        self._X_train = []
        self._y_train = []

    def fit(self, X_train, y_train):
        self._X_train = X_train
        self._y_train = y_train

    def predict(self, X_test):
        return [self.closet(x) for x in X_test]

    def closet(self, x):
        from scipy.spatial import distance

        indexed_distances = [ (index, distance.euclidean(x, t)) for index, t in enumerate( self._X_train ) ]
        indexed_distances.sort(key=lambda x: x[1])

        return self._y_train[indexed_distances[0][0]]

accuracy_of(KNN())
