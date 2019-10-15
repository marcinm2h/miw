from __future__ import annotations # https://stackoverflow.com/questions/15853469/putting-current-class-as-return-type-annotation
from typing import List, Tuple
from functools import reduce

def create_empty_2dArray(row: int, col: int) -> List[List[int]]:
  return [[0]*col]*row

class Matrix:
  __value: List[List[int]]

  def __init__(self, value: List[List[int]]) -> None:
    self.__value = value
  
  def print(self) -> None:
    print(self.__value)
  
  def get_dimensions(self) -> Tuple[int, int]:
    return (len(self.__value), len(self.__value[0]))
  
  def has_equal_rows(self) -> bool:
    return reduce(lambda acc, row: acc and len(row) == len(self.__value[0]), self.__value, True)

  def multiply(self, other: Matrix) -> Matrix:
    if not self.has_equal_rows() or not other.has_equal_rows():
      raise ValueError("Can not multiply matrices wihich rows aren't equal")

    if self.get_dimensions() != other.get_dimensions():
      raise ValueError("Can not multiply matrices of non matching dimensions")

    [row, col] = self.get_dimensions()
    result_array: List[List[int]] = create_empty_2dArray(row, col)

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

m3 = matrix_1.multiply(matrix_2)

m3.print()
