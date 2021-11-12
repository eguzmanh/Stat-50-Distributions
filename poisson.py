import math

from action_utils import choose_action, set_action_bounds


""" Poisson Formulas """
def Poisson(l, x):
    if x >= 0 and int(x) - x == 0:
        return math.exp(-1 * l) * (l ** x) / math.factorial(x)
    else:
        return 0

def PoissonGT(l, x):
    sub = 1
    for i in range(int(x+1)):
        sub -= Poisson(l,i)
    return sub

def PoissonLT(l, x):
    return PoissonLTEQ(l, x - 1.0)

def PoissonLTEQ(l, x):
    sum = 0
    for i in range(int(x + 1)):
        sum += Poisson(l,i)
    return sum
""" ####################################### """

def action_prompt():
    print("""
            Choose action
        ----------------------
        0. Poisson(X = x)
        1. Poisson(X > x)
        2. Poisson(X < x)
        3. Poisson(X <= x)
    """)
    action_bounds = set_action_bounds(0, 3)
    return choose_action(action_bounds)

def exec_poisson():
    poiss_arr = [Poisson, PoissonGT, PoissonLT, PoissonLTEQ]
    id = action_prompt()
    l = float(input("Enter the lambda value: "))
    x = float(input("Enter the x value: "))

    return poiss_arr[id](l, x)
