"""
Choosing good features is one of your most important jobs.
"""


import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()

# print(iris.feature_names)
# print(iris.target_names)
# print(iris.data[:10])
# print(iris.target[:10])

# one of each kind of iris
test_indexes = [
    0,
    50,
    100,
]

# traning_data

train_data = np.delete(iris.data, test_indexes, axis=0)
train_target = np.delete(iris.target, test_indexes)

# testing_data

test_data = iris.data[test_indexes]
test_target = iris.target[test_indexes]

# train classifier

classifier = tree.DecisionTreeClassifier()
classifier.fit(train_data, train_target)

print(test_target)
print(classifier.predict(test_data))
