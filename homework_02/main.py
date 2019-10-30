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

  def fit(self, x1: float, x2: float, x3: float, x4: float):
    th1, th2, th3, th4, th5 = self.__theta.T.tolist()[0]
    return th1*x1 + th2*x2 + th3*x3 + th4*x4 + th5

if __name__ == "__main__":
  data: np.ndarray = np.genfromtxt(
    "iris.csv",
    delimiter=",",
    names=("sepal_length", "sepal_width", "petal_length", "petal_width", "species"),
    dtype=None,
    encoding="UTF-8",
    skip_header=1,
  )
  np.random.shuffle(data)

  training_data = data[:120]
  test_data = data[120:]

  X: np.matrix = np.matrix(
    training_data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].tolist()
  )
  # col k+1: fill with ones
  X: np.matrix = np.hstack((X, np.ones((X.shape[0], 1))))

  mapping = {
    "Iris-setosa": 1,
    "Iris-versicolor": 2,
    "Iris-virginica": 3,
  }

  y: np.matrix = np.matrix(
    list(map(lambda x: mapping[x[0]], training_data[['species']]))
  ).T

  model: Linear_Regression = Linear_Regression(X, y)

  print(model.fit(5.1,3.5,1.4,.2)) # Iris-setosa - 1
  print(model.fit(5.2,2.7,3.9,1.4)) # Iris-versicolor - 2
  print(model.fit(6.3,3.4,5.6,2.4)) # Iris-virginica - 3
