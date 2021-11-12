def choose_action(bounds): 
    action = -1
    # change the action < 3 to number of actions
    while True:
        try:
            action = int(input("choose the action: "))
            if (action < bounds["lower"] or action > bounds["upper"]):
                raise ValueError
            break
        except ValueError:
            print(f"Your bounds are: ({bounds['lower']}, {bounds['upper']})\n\n")
    return action

def set_action_bounds(l, b):
    return {"lower" : l, "upper": b}