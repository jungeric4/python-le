from __future__ import division
from sympy import *
init_printing(use_unicode=True)


V18d, C18, R13, R15, R19, V18, R16, R14, V10, V12 = symbols('V18d, C18, R13, R15, R19, V18, R16, R14, V10, V12')
M = Matrix([V18d])
A = (-1) / (C18 * (R13 + R15)) - (1) / (C18 * R19)
q = Matrix([V18])
B = (1) / (C18 * (R13 + R15)) - (1) / (C18 * R13) * (R16) / (C18 * R13 * (R14 + R16))
u = Matrix([V10, V12])
