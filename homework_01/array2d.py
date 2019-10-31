from typing import List

Array2d = List[List[int]]

def create_empty_2d_array(row: int, col: int) -> Array2d:
  return [[0 for x in range(col)] for y in range(row)]
