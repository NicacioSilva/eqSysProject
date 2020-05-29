from sympy import *

def sys_2x2(a1, b1, c1, a2, b2, c2):
    coefficients = {
        'a1': a1,
        'b1': b1,
        'c1': c1,
        'a2': a2,
        'b2': b2,
        'c2': c2,
    }
    system = Matrix(((a1, b1, c1), (a2, b2, c2)))
    dictionary = solve_linear_system(system, 'x', 'y')
    dictionary.update(coefficients)
    x, y = symbols('x y')
    expr_1 = latex(a1 * x + b1 * y)
    expr_2 = latex(a2 * x + b2 * y)
    expression = {'expr_1': expr_1, 'expr_2': expr_2}
    dictionary.update(expression)
    return dictionary
