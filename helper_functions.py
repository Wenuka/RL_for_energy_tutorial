import numpy as np


def espilon_decreasing_greedy(action, epsilon, nb_action):
    
    p = np.random.random()

    if p < (1 - epsilon):
        randomm=0
        return action, randomm

    else: 
        randomm=1
        return np.random.choice(nb_action), randomm


def max_dict(d):

    max_key = None
    max_val = float('-inf')


    for k,v in d.items():

        if v > max_val:

            max_val = v
            max_key = k

    return max_key, max_val


def update_epsilon(epsilon):
    
    epsilon = epsilon - epsilon *0.02
    
    if epsilon < 0.1:
        
        epsilon = 0.1
    
    return epsilon


def change_name_action(idx):
    #action 0: battery_charge
    #action 1: battery_discharge
    #action 2: grid_import
    #action 3: grid_export
    
    if idx == 0:       
        action_name = "charge"
    elif idx == 1:
        action_name = "discharge"
    elif idx == 2:
        action_name = "import"
    else:
        action_name = "export"
    
    return action_name


def print_welcome(idx):
    
    if idx == 0:
        print("------------------------------------")
        print("|        WELCOME TO PYMGRID        |")
        print("------------------------------------")
    elif idx == 1:
        print("t -     STATE  -  ACTION - COST")
        print("================================")
        

def custom_round(x, base=1):
    return int(base * round(x/base))
    