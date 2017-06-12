from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

# set up

iris = load_iris()

# f(X) = y
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5)

decision_tree_classifier = tree.DecisionTreeClassifier()

def accuracy_of(classifier):
    classifier.fit(X_train, y_train)

    predictions = classifier.predict(X_test)

    print(accuracy_score(y_test, predictions))

accuracy_of(tree.DecisionTreeClassifier())
accuracy_of(KNeighborsClassifier())
