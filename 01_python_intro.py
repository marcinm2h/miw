from typing import List, Dict, Tuple, Set
from functools import reduce

a: int = 1
b: float = 2.5
c: bool = True
d: bool = False
e: List[int] = [1, 2, 3]
g: Tuple[int, int, int] = (1, 2, 3)
h = 1, 2, 3
k, m, d = 1, 2, 3
d: Dict[str, int] = { "a": 1, "b": 2 }
t: List = [1, True, "b"]
i: str = "g"
c: str = 'c'
s: Set[int] = { 1, 2, 3 }

d: Dict[str, int] = dict(a=1, b=2)

print(g)
print(type(""))
print(type(''))

w: List[int] = ["ala", "ma", True]


class A:
  __a: int
  _b: int
  c: str
  def __init__(self, a: int = 11):
    self.__a = a
  
  def print_and_get_a(self) -> int:
    print(self.__a)
    return self.__a
  
  @staticmethod
  def a(): #jak static
    return "a"

  @staticmethod
  def b():
    pass

a = A()
a.print_and_get_a()
print(a._A__a)
# print(a.a)
print(dir(a))

del a

x = A.b()

print(x)


for i in range(1):
  print(i)
for i in range(1, 10):
  print(i)
for i in range(1, 10, 2):
  print(i)
for i in range(10, 1, -1):
  print(i)

a: List[int] = [1, 2, 4, 5]

a.__iter__()

for i in a:
  print(i)

for i in a[::-1]:
  print(i)

for index, value in enumerate(a):
  print(f"{index}, {value}")

s: str = "{}, {}".format(1, 2)
print(s)
s: str = f"{s}, {i + 3}"
print(s)

a: List[int] = [1, 2, 3, 4, 5]
b: List[int] = [6, 7, 8]

for i, j in zip(a, b):
  print(f"i: {i}, j: {j}")


i: int = 0

while i < 10:
  print(i)
  i += 1

a: List[int] = [1, 2, 3]

print(a + a)
print(2 * a)

class B:
  __b: int

  def __init__(self, b: int = 11):
    self.__b = b

# b: List[A] = [A()] * 20

# print(b)



x: List[int] = [1, 2, 3]
y: List[int] = [i + 1 for i in a if i >1]

print(y)

if ("2" == 2):
  print("'2' == 2")
else:
  print("'2' not == 2")

class X:
  __x: int

  def __int__(self, x: int = 100):
    self.__x = x

  # def __eq__(self, other) -> bool:
  #   return self.__x == other.__x


x1 = X()
x2 = X()

print(x1 == x2)


if 1 == 2:
  print("1 == 2")
elif 2 == 3:
  print("??")
else:
  print("X")

class D:
  def f(self) -> int:
    raise NotImplementedError

class G(D):
  def f(self) -> int:
    print("F here")

d = D()
try:
  d.f()
except NotImplementedError:
  print("NotImplementedError")

g = G()
g.f()

a: List[int] = [1, 2, 3, 4, 5, 6]

print(a[-1])
print(a.pop())
del a[0]
print(a)
print(len(a))

print(a.index(2))
a.append(0)
a += [0]


# array slicing

a: List[int] = [1, 2, 3, 4, 5, 6]
print(a[-1::])
print(a[-2:-1:1])
print(a[-2:-1:-1]) # 
print(a[2:-1])
print(a[2:-1:2]) # co 2 elementy


str = "test jak to działa"
print(str[-1:0:-1])

try:
  f = open("data.csv", "r")

  all_lines = f.read()

  f.close()
except Exception:
  print("Brak pliku")


# with open("data.csv", "r") as f:
#     all_lines: List[str] = f.readlines()


print(globals())
print(locals())

def f():
  global x
  x = 100

print(x)
f()
print(x)

if True:
  a: int = 1

print(a)


print(reduce(lambda left, right: left + right, [1, 2, 3]))

# TODO: Zaimplementować bez użycia bibliotek

# Mnożenie macierzy
# Transpozycja macierzy
# Iloczyn skalarny

import numby as np
a: np.ndarray = np.linspace(0,9).reshape(3, 3)
b: np.ndarray = np.arrange(15).reshape(3, 5)
c: np.ndarray = np.random.uniform(size=3)
d: np.ndarray = np.random.uniform(size=3)


print(a @ b)
print(a.T)
print(c @ d)

import numpy as np

a = np.matrix([
  [-1, -2, 3],
  [0, 2, -1],
  [-1, 3, 0]
])
b = np.matrix([
  [1, 5, 1],
  [2, 1, 2],
  [3, 2, 3]
])
c = np.matrix([
  [1, 5, 1],
  [3, 2, 3]
])

print(a * b)
# print(a * c)