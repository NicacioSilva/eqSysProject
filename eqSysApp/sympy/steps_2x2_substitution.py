from sympy import *

'''
steps = [
    {
        'step_name': 'step 1',
        'step_body': ['body 1', 'body 2', 'body 3', 'body 4'],
    },
    {
        'step_name': 'step 2',
        'step_body': ['body 1', 'body 2'],
    },
    {
        'step_name': 'step 3',
        'step_body': ['body 1'],
    },
    {
        'step_name': 'step 4',
        'step_body': ['body 1', 'body 2', 'body 3'],
    }
]
'''


def system_2x2_solution_steps(a1, b1, c1, a2, b2, c2):
    x, y = symbols('x y')
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
             f'{latex(a2 * UnevaluatedExpr((c1 - b1 * y) / (a1)))}' + \
             f'{latex( + b2 * y)}' + \
             r'& = ' + \
             f'{c2}' + \
             r'\end{align}'

    step_body.append(body_1)
    steps.append({'step_name': step_name, 'step_body': step_body})

    return steps
