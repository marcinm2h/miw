from typing import List, Tuple
import numpy as np

class Linear_Regression:
  def __init__(self, X: np.matrix, y: np.matrix) -> None:
    self.__X = X
    self.__y = y
    self.__theta = self.__calc_theta()

  def __calc_theta(self) -> np.matrix:
    X = self.__X
    y = self.__y

    return np.linalg.inv(X.T.dot(X)).dot(X.T.dot(y))

  def fit(self, x: List[float]) -> float:
    x1, x2, x3, x4 = x
    th1, th2, th3, th4, th5 = self.__theta.T.tolist()[0]

    return th1*x1 + th2*x2 + th3*x3 + th4*x4 + th5

if __name__ == "__main__":
  def prepare_iris_data(iris_data: np.ndarray) -> Tuple[np.matrix, np.matrix]:
    X: np.matrix = np.matrix(
      iris_data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].tolist()
      )
    # col k+1: fill with ones
    X: np.matrix = np.hstack((X, np.ones((X.shape[0], 1))))
    mapping = {
      "Iris-setosa": 1,
      "Iris-versicolor": 2,
      "Iris-virginica": 3,
    }

    y: np.matrix = np.matrix(
      list(map(lambda x: mapping[x[0]], iris_data[['species']]))
    ).T

    return X, y

  data: np.ndarray = np.genfromtxt(
    "iris.csv",
    delimiter=",",
    names=("sepal_length", "sepal_width", "petal_length", "petal_width", "species"),
    dtype=None,
    encoding="UTF-8",
    skip_header=1,
  )
  np.random.seed(0) # for predictable results
  np.random.shuffle(data)

  training_data: np.ndarray = data[:120]
  test_data: np.ndarray = data[120:]

  X, y = prepare_iris_data(training_data)

  model: Linear_Regression = Linear_Regression(X, y)

  print(f"{model.fit([5.1,3.5,1.4,.2])}, expected Iris-setosa -> 1")
  print(f"{model.fit([5.2,2.7,3.9,1.4])}, expected Iris-versicolor -> 2")
  print(f"{model.fit([6.3,3.4,5.6,2.4])}, expected Iris-virginica -> 3")


  def get_r_squared(model: Linear_Regression, X: np.matrix, y: np.matrix) -> float:
    nominator: float = 0
    denominator: float = 0
    y_list: List[List[float]] = y.tolist()
    y_avg: float = np.average(y_list)

    for idx, x in enumerate(X.tolist()):
      nominator += (model.fit(x[:4]) - y_list[idx][0]) ** 2
      denominator += (y_avg - y_list[idx][0]) ** 2

    return 1 - (nominator/denominator)

  X, y = prepare_iris_data(test_data)
  r_squared = get_r_squared(model, X, y)
  print(r_squared)
