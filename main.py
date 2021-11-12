from exponential import exec_exponential
from poisson import exec_poisson
from action_utils import choose_action, set_action_bounds

# Functions for the actions

# prompt user
def action_prompt():
    print("""
        Choose a Distribution
        ----------------------
        0. quit
        1. Poisson
        2. Exponential
    """)
    action_bounds = set_action_bounds(0,2)
    id = choose_action(action_bounds)
    return exec_distribution(id)



# Add actions to this function
def exec_distribution(id):
    result = 0
    if id == 0:
        quit()
        return
    elif id == 1:
        result = exec_poisson()
    elif id == 2:
        result = exec_exponential()

    return decimal_precision(result) 

#######################################

# Request desired value
def decimal_precision(result):
    dec_lim = 0
    while True:
        try: 
            dec_lim = int(input("# of decimals places: "))
            if dec_lim < 1 or dec_lim > 7:
                raise ValueError
            break
        except ValueError:
            print("ERROR: You must enter a number between 1 & 7!\n")

    return f'{result:.{dec_lim}f}'

def quit():
    return "Exiting program ...\n\Goodbye."

            
if __name__ == "__main__":
    cont = 'y'
    while (cont.upper() == "Y"):
        result = action_prompt()
        print(result)
        cont = str(input("Do you have another input? ('y'/'n'): "))

