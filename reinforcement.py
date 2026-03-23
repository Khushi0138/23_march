import numpy as np
import random
q=np.zeros((4,4))  #Q-table
print(q)  
alpha=0.1
gamma=0.9
epsilon=0.2

#Reward function
def get_reward(state):
    if state==3:
        return 1
    return 0

#Next state logic (simple)
def get_next_state(state, action):
    if action==3 and state < 3:
        return state+1
    elif action==1 and state < 2:
        return state+2
    return state

#Training 

