import numpy as np
import math
import sympy as sp
from sympy import *
from scipy import integrate

#Функция для интеграла Scipy
def f(x):
    return 1/(x**2 + 4*x + 9) 

#1
numbers = np.random.uniform(-3 + 1e-15, 3, (5, 5))
numbers.transpose()
determinant = np.linalg.det(numbers)
print("Определитель вещественной транспонированной матрицы")
print(determinant, '\n\n')

#3
x, y = symbols('x, y')
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
print(res, '\n\n')

#5
a = np.array([[-7, -5, -5], [0, 3, 0], [10, 5, 8]], int)
vals, vecs = np.linalg.eig(a)
print("Собственные значения")
print(vals)
print("Собственные вектора")
print(vecs, '\n\n')

#7
resForIntegrate1, err = integrate.quad(f, -np.inf, np.inf)
print("Вычисленный интеграл при помощи SciPy и погрешность")
print(resForIntegrate1, err)

x = Symbol('x')
exprForIntegrate = 1/(x**2 + 4*x + 9)
resForIntegrate2 = sp.integrate(exprForIntegrate, (x, -sp.oo, sp.oo))
print("Вычисленный интеграл при помощи SymPy символьно и численно")
print(resForIntegrate2)
print(resForIntegrate2.evalf(), '\n\n')

