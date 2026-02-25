import numpy as np
import math
from sympy import *

#1
numbers = np.random.uniform(-3 + 1e-15, 3, (5, 5))
numbers.transpose()
determinant = np.linalg.det(numbers)

print(determinant)

#3
x, y = symbols('x y')
expr = (7*x*y)/4 * (x + y) - (x - y)**2
print("=============Ваше выражение===========")
pprint(expr)
print("==========Упрощённое выражение========")
new_expr = simplify(expr)
pprint(new_expr)
print("===============Результат==============")

val_x = -1.23
val_y = math.sqrt(8)
res = new_expr.subs({x: val_x, y: val_y})
print(res)

#5
a = np.array([[-7, -5, -5], [0, 3, 0], [10, 5, 8]], int)
vals, vecs = np.linalg.eig(a)
print(vals)
print(vecs)
