from sympy import *
import math


def sys_2x2(a1, b1, c1, a2, b2, c2):
    coefficients = {
        'a1': dec_to_int(a1),
        'b1': dec_to_int(b1),
        'c1': dec_to_int(c1),
        'a2': dec_to_int(a2),
        'b2': dec_to_int(b2),
        'c2': dec_to_int(c2),
    }
    system = Matrix(((a1, b1, c1), (a2, b2, c2)))
    dictionary = solve_linear_system(system, 'x', 'y')

    x, y = symbols('x y')
    expr_1 = latex(dec_to_int(a1) * x + dec_to_int(b1) * y)
    expr_2 = latex(dec_to_int(a2) * x + dec_to_int(b2) * y)
    expression = {'expr_1': expr_1, 'expr_2': expr_2}

    dictionary.update(coefficients)
    dictionary.update(expression)
    return dictionary


def dec_to_int(number):
    dec, num = math.modf(number)
    if dec == 0:
        return int(number)
    else:
        return number
