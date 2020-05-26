from typing import Dict, List, Any, Union

from sympy import Matrix, solve_linear_system


def sys_2x2(a1, b1, c1, a2, b2, c2):
    system = Matrix(((a1, b1, c1), (a2, b2, c2)))
    dictionary = solve_linear_system(system, 'x', 'y')
    return dictionary
