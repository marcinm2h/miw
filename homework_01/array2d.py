from typing import List

Array2d = List[List[int]]

def create_empty_2d_array(row: int, col: int, val: int = 0) -> Array2d:
  return [[val for x in range(col)] for y in range(row)]
