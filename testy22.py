from __future__ import division
from sympy import *
init_printing(use_unicode=True)

#assign varibles
V18d, C18, R13, R15, R19, V18, R16, R14, R5, R3, R4, R2, R9, R8, R7, V4r, V5r, V1 = symbols('V18d, C18, R13, R15, R19, V18, R16, R14, R5, R3, R4, R2, R9, R8, R7. V4r, V5r, V1')

#state equation matrix
M = Matrix([V18d])

A = (-1) / (C18 * (R13 + R15)) - (1) / (C18 * R19)
q = Matrix([V18])
B = (1) / (C18 * (R13 + R15)) - (1) / (C18 * R13) * (R16) / (C18 * R13 * (R14 + R16))

u = Matrix([V1])

#separate B and MCB to make calculation easier
V4r = (R4) / (R4 + R2)
V5r = (R5) / (R5 + R3)
MCB = (V5r + (V4r - V5r)*(R9/R8)) + (V4r - (V4r - V5r)*(R7/R8))

#final matrix
M = A * q + B * MCB * u
