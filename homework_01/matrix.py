from __future__ import annotations # https://stackoverflow.com/questions/15853469/putting-current-class-as-return-type-annotation
from typing import List, Tuple
from functools import reduce
from array2d import create_empty_2d_array, Array2d

class Matrix:
  __array: Array2d

  def __init__(self, array: Array2d) -> None:
    self.__array = array
  
  def get_array(self) -> Array2d:
    return self.__array
  
  def get_dimensions(self) -> Tuple[int, int]:
    rows: int = len(self.__array)
    cols: int = len(self.__array[0])
    return (rows, cols)
  
  def has_equal_rows(self) -> bool:
    return reduce(lambda acc, row: acc and len(row) == len(self.__array[0]), self.__array, True)

  def multiply(self, other: Matrix) -> Matrix:
    if not self.has_equal_rows() or not other.has_equal_rows():
      raise ValueError("Can not multiply matrices wihich rows aren't equal")

    if self.get_dimensions() != other.get_dimensions():
      raise ValueError("Can not multiply matrices of non matching dimensions")

    [curr_rows, curr_cols] = self.get_dimensions()
    result_array: Array2d = create_empty_2d_array(curr_rows, curr_cols)
    for row_idx in range(curr_rows):
      for col_idx in range(curr_cols):
        result: int = 0
        for idx in range(curr_cols):
          result += self.__array[row_idx][idx] * other.__array[idx][col_idx]
        result_array[row_idx][col_idx] = result

    return Matrix(result_array)
  
  def transpoze(self) -> Matrix:
    [curr_rows, curr_cols] = self.get_dimensions()
    result_array: Array2d = create_empty_2d_array(curr_cols, curr_rows)
    for row_idx in range(len(result_array)):
      for col_idx in range(len(result_array[row_idx])):
        result_array[row_idx][col_idx] = self.__array[col_idx][row_idx]

    return Matrix(result_array)

class Vector:
  __array: List[int]

  def __init__(self, array: List[int]) -> None:
    self.__array = array

  def dot_product(self, other: Vector) -> int:
    if len(self.__array) != len(other.__array):
      raise ValueError("Can not preform operation for uneven vecotrs")

    result: int = 0
    for idx in range(len(self.__array)):
      result += self.__array[idx] * other.__array[idx]

    return result

if __name__ == "__main__":
  matrix_1 = Matrix([
    [-1, -2, 3],
    [0, 2, -1],
    [0, 2, -1],
    [-1, 3, 0]
  ])
  matrix_2 = Matrix([
    [1, 5, 1],
    [2, 1, 2],
    [2, 1, 2],
    [3, 2, 3]
  ])

  # multiplication
  multiplication_result = matrix_1.multiply(matrix_2)
  print(multiplication_result.get_array())

  # transposition
  transposition_result_1 = matrix_1.transpoze()
  transposition_result_2 = Matrix([[0,1], [2,3], [4,5]]).transpoze()
  print(transposition_result_1.get_array())
  print(transposition_result_2.get_array())

  # dot product
  vector_1 = Vector([1, 2, 3])
  vector_2 = Vector([3, 4, 5])
  print(vector_1.dot_product(vector_2))
