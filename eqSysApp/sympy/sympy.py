import math

from sympy import *


def sys_manager(dic):
    count_coefficients = str(len({key: value for (key, value) in dic.items() if len(key) == 2}))

    def system(x):
        return {
            '6': sys_2x2(dic)
        }.get(x, {'error': 'error'})

    return system(count_coefficients)


def sys_2x2(dic):
    coefficients, (a1, b1, c1, a2, b2, c2) = load_coefficients(dic)

    m = Matrix([[a1, b1], [a2, b2]])

    dictionary = {}
    if m.det() != 0:
        system = Matrix(((a1, b1, c1), (a2, b2, c2)))
        dictionary = solve_linear_system(system, 'x', 'y')
        dictionary.update({'message': 'Successfully solved!'})
        from eqSysApp.sympy.steps_2x2_substitution import system_2x2_solution_steps
        steps = system_2x2_solution_steps(a1, b1, c1, a2, b2, c2)
        dictionary.update({'steps': steps})
    else:
        dictionary.update({'message': 'The system has no solution or it is indeterminate.'})

    x, y = symbols('x y')
    expr_1 = latex(a1 * x + b1 * y)
    expr_2 = latex(a2 * x + b2 * y)
    expression = {'expr_1': expr_1, 'expr_2': expr_2}

    dictionary.update(coefficients)
    dictionary.update(expression)
    return dictionary


def dec_to_int(number):
    dec, num = math.modf(float(number))
    if dec == 0:
        return int(number)
    else:
        return number


def load_coefficients(dic):
    coefficients = {}
    values = []
    for key, value in dic.items():
        if len(key) == 2:
            coefficients[key] = dec_to_int(value)
            values.append(coefficients[key])

    return coefficients, tuple(values)
