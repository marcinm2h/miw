from __future__ import annotations # https://stackoverflow.com/questions/15853469/putting-current-class-as-return-type-annotation
from typing import List, Tuple
from functools import reduce

Array2d = List[List[int]]

def create_empty_2d_array(row: int, col: int) -> Array2d:
  return [[0 for x in range(row)] for y in range(col)]

class Matrix:
  __array: Array2d

  def __init__(self, value: Array2d) -> None:
    self.__array = value
  
  def get_array(self) -> Array2d:
    return self.__array
  
  def get_dimensions(self) -> Tuple[int, int]:
    return (len(self.__array), len(self.__array[0]))
  
  def has_equal_rows(self) -> bool:
    return reduce(lambda acc, row: acc and len(row) == len(self.__array[0]), self.__array, True)

  def multiply(self, other: Matrix) -> Matrix:
    if not self.has_equal_rows() or not other.has_equal_rows():
      raise ValueError("Can not multiply matrices wihich rows aren't equal")

    if self.get_dimensions() != other.get_dimensions():
      raise ValueError("Can not multiply matrices of non matching dimensions")

    [rows, cols] = self.get_dimensions()
    result_array: Array2d = create_empty_2d_array(rows, cols)
    for row_idx in range(rows):
      for col_idx in range(cols):
        result: int = 0
        for idx in range(rows):
          result += self.__array[row_idx][idx] * other.__array[idx][col_idx]
        result_array[row_idx][col_idx] = result

    return Matrix(result_array)


matrix_1 = Matrix([
  [-1, -2, 3],
  [0, 2, -1],
  [-1, 3, 0]
])

matrix_2 = Matrix([
  [1, 5, 1],
  [2, 1, 2],
  [3, 2, 3]
])

multiplication_result = matrix_1.multiply(matrix_2)

print(multiplication_result.get_array())
