from sympy import *
import math

def sys_manager(**kwargs):
    ''' It receives the args and decides what system function
        will process everything returns a dictionary with the
        appropriate content. '''
    pass

def sys_2x2(dic):
    a1 = dic.get('a1')
    b1 = dic.get('b1')
    c1 = dic.get('c1')
    a2 = dic.get('a2')
    b2 = dic.get('b2')
    c2 = dic.get('c2')
    a1, b1, c1, a2, b2, c2 = dec_to_int(a1), dec_to_int(b1), dec_to_int(c1), dec_to_int(a2), dec_to_int(b2), dec_to_int(c2)
    coefficients = {
        'a1': a1,
        'b1': b1,
        'c1': c1,
        'a2': a2,
        'b2': b2,
        'c2': c2,
    }
    # test if linear system have a solution and validate:
    # if yes: call the steps function and pass the params
    # if not: return an advise message.
    system = Matrix(((a1, b1, c1), (a2, b2, c2)))
    dictionary = solve_linear_system(system, 'x', 'y')

    x, y = symbols('x y')
    expr_1 = latex(a1 * x + b1 * y)
    expr_2 = latex(a2 * x + b2 * y)
    expression = {'expr_1': expr_1, 'expr_2': expr_2}

    dictionary.update(coefficients)
    dictionary.update(expression)
    return dictionary


def dec_to_int(number):
    dec, num = math.modf(float (number))
    if dec == 0:
        return int(number)
    else:
        return number
