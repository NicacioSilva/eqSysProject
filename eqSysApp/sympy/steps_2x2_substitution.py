from sympy import *

def system_2x2_solution_steps(a1, b1, c1, a2, b2, c2):
    x, y = symbols('x y')
    system = Matrix(((a1, b1, c1), (a2, b2, c2)))
    solution = solve_linear_system(system, 'x', 'y')
    solution_x, solution_y = solution.values()
    steps = []

    step_name = 'Step 1'
    step_body = []
    body_1 = ''
    if a1 != 0:
        body_1 = r'\begin{align} \text{Isolate x for equation (i): }' + \
                 f'{latex(a1 * x + b1 * y)}' + \
                 r'& =' + \
                 f'{c1} ' + \
                 r'\Rightarrow' + \
                 r'\\ x & =' + \
                 f'{latex(factor((c1 - b1 * y) / (a1)))}' + \
                 r'\end{align}'
        step_body.append(body_1)
    steps.append({'step_name': step_name, 'step_body': step_body})

    step_name = 'Step 2'
    step_body = []
    body_1 = r'\begin{align} \text{Substitute x: }' + \
             r' x & =' + \
             f'{latex(factor((c1 - b1 * y) / (a1)))}' + \
             r'\text{ in the equation (ii): }' + \
             r'\\' + \
             f'{latex(a2 * UnevaluatedExpr((c1 - b1 * y) / (a1)))} + ' + \
             f'{latex(b2 * y)}' + \
             r'& = ' + \
             f'{c2}' + \
             r'\\' + \
             f'{latex(a2 * (c1 - b1 * y) / (a1))} + ' + \
             f'{latex(b2 * y)}' + \
             r'& = ' + \
             f'{c2}' + \
             r'\\' + \
             f'{latex(a2 * (c1 - b1 * y) / (a1) + b2 * y)}' + \
             r'& = ' + \
             f'{c2}' + \
             r'\end{align}'

    body_2 = r'$$ \bbox[5px,border:2px solid black]{' + \
             f'{latex(simplify(Eq(a2 * (c1 - b1 * y) / (a1) + b2 * y, c2)))}' + \
             r'}$$'

    step_body.append(body_1)
    step_body.append(body_2)
    steps.append({'step_name': step_name, 'step_body': step_body})

    step_name = 'Step 3'
    step_body = []

    body_1 = r'\begin{align} \text{As we know x by: }' + \
             r' x & =' + \
             f'{latex(factor((c1 - b1 * y) / (a1)))}' + \
             r'\therefore \text{by substituting y} \implies' + \
             r'\\' + \
             r' x & =' + \
             f'{c1}' + \
             f'{latex(-b1 * solution_y)}' + \
             r'\end{align}'

    body_2 = r'$$ \bbox[5px,border:2px solid black]{ x = ' + \
             f'{latex(solution_x)}' + \
             r'}$$'

    step_body.append(body_1)
    step_body.append(body_2)
    steps.append({'step_name': step_name, 'step_body': step_body})

    return steps