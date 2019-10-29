import numpy as np

# https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/

training_data: np.ndarray = np.loadtxt("iris_c.csv", delimiter=";", dtype={'names': ('sepal_length','sepal_width','petal_length','petal_width','type'), 'formats': ('f', 'f', 'f', 'f', 'f')})
iris_l: np.ndarray = np.loadtxt("iris_l.csv", delimiter=";", dtype={'names': ('sepal_length','sepal_width','petal_length','petal_width','type'), 'formats': ('f', 'f', 'f', 'f', 'f')})

# for index, row in enumerate(training_data):
#     print(row)

import math

def euclidean_distance(instance1, instance2, take):
    distance = 0
    for x in range(take):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)

data1 = [2, 2, 2, 'a']
data2 = [4, 4, 4, 'b']
distance = euclidean_distance(data1, data2, 3)
print(f"Distance: {distance}")


# TODO: napisać 1 stronę raportu
# - k = 3 -> 3 najbliższych sąsiadów, dla szukanego elementu

