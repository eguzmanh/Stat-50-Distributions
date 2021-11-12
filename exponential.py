import math

from action_utils import choose_action, set_action_bounds


""" Exponential Formulas """
exp = lambda l,x : math.exp((-1*l*x)) if x > 0 else 0

def Exponential(l,x):
    return l * exp(l, x)

def ExponentialGT(l,x):
    return exp(l, x)

def ExponentialLT(l,x):
    return ExponentialLTEQ(l, x-1.0)

def ExponentialLTEQ(l,x):
    return 1.0 - exp(l, x)
""" ####################################### """

def action_prompt():
    print("""
            Choose action
        ----------------------
        0. Exp(X = x)
        1. Exp(X > x)
        2. Exp(X < x)
        3. Exp(X <= x)
    """)
    action_bounds = set_action_bounds(0, 3)
    return choose_action(action_bounds)

def exec_exponential():
    exp_arr = [Exponential, ExponentialGT, ExponentialLT, ExponentialLTEQ]
    id = action_prompt()
    l = float(input("Enter the lambda value: "))
    x = float(input("Enter the x value: "))

    return exp_arr[id](l, x)

