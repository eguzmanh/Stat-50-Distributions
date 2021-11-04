import math

# Functions for the actions

# prompt user
def action_prompt():
    print("""
        choose an action
        ---------------------
        1. P(X = x)
        2. P(X > x)
        3. P(X < x)
        4. P(X <= x) 
        5. Exp(X = x)
        6.Exp(X > x)
        7. Exp(X < x)
        8. Exp(X <= x)
    """)
    id = action_choice()
    return action_execution(id)


def action_choice(): 
    action = -1
    # change the action < 3 to number of actions
    while not (action < 9 and action > 0):
        action = int(input("choose the action: "))
        return action

# Add actions to this function
def action_execution(id):
    result = 0
    p = float(input("Enter the lambda value: "))
    x = float(input("Enter the x value: "))
    
    if id == 1:
        result = Poisson(p, x)
    elif id == 2:
        result = PoissonGT(p, x)
    elif id == 3:
        result = PoissonLT(p, x)
    elif id == 4:
        result = PoissonLTEQ(p, x)
    elif id == 5:
        result = Exponential(p, x) 
    elif id == 6:
        result = ExponentialGT(p, x) 
    elif id == 7:
        result = ExponentialLT(p, x)
    elif id == 8:
        result = ExponentialLTEQ(p, x)
        
    return "{:.4f}".format(result)  # returns 4 decimal places

#######################################


""" Functions for Formulas """

# Poisson Dist
def Poisson(l, x):
    if x > 0:
        return ( math.exp(-1 * l)*(l ** x) )/(math.factorial(x) ) 
    else:
        return 0

def PoissonGT(l, x):
    sub = 1
    for i in range(int(x)+1):
        sub -= Poisson(l,i)
    return sub

def PoissonLT(l, x):
    return PoissonLTEQ(l, x-1.0)

def PoissonLTEQ(l, x):
    sum = 0
    for i in range(int(x+1)):
        sum += Poisson(l,i)
    return sum
########################################

# Exponential Dist
def Exponential(l,x):
    return l * math.exp((-1*l*x)) if x > 0 else 0
def ExponentialGT(l,x):
    return math.exp(-1*l*x) if x > 0 else 0
def ExponentialLT(l,x):
    return ExponentialLTEQ(l, x-1.0)
def ExponentialLTEQ(l,x):
    return 1.0 - math.exp(-1*l*x) if x > 0 else 0

#######################################
            
if __name__ == "__main__":
    cont = 'y'
    while (cont.upper() == "Y"):
        result = action_prompt()
        print(result)
        cont = str(input("Do you have another input? ('y'/'n'): "))

