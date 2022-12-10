import pandas as pd
import numpy as np
import time
from cube_enviroment import cube
import csv
action = ["F","F'","R","R'","B","B'","L","L'","U","U'","D","D'"]
#table = pd.DataFrame(np.zeros((10,12)), columns= action)
solved = list(range(0,54))
np.random.seed(2) # reproducible
N_STATES = 6 # the length of the 1 dimensional world
ACTIONS = ["F","F'","R","R'","B","B'","L","L'","U","U'","D","D'"] # available actions
EPSILON = 0.9 # greedy police
ALPHA = 0.2 # learning rate
GAMMA = 0.9 # discount factor
MAX_EPISODES = 10 # maximum episodes
FRESH_TIME = 0.1 # fresh time for one move

with open('training_set.csv', 'r') as f:
    reader = csv.reader(f)
    result = [[int(element) for element in row ]for row in reader]
    training = result


def build_q_table(n_states, actions):
    #table = pd.DataFrame(np.zeros((len(n_states), len(actions))), columns=actions)
    #table.to_csv('q_table_reinforce_4timesshuffle_1.csv', index=False, header=True)
    table = pd.read_csv("q_table_reinforce_4timesshuffle_1.csv")
    print(table) # show table
    return table

def choose_action(state, q_table):
    # This is how to choose an action
    state_actions = q_table.iloc[training.index(state), :]
    if (np.random.uniform() > EPSILON) or (state_actions.all() == 0): # act non-greedy or state-action have no value
        action_name = np.random.choice(ACTIONS)
    else: # act greedy
        action_name = state_actions.idxmax()
    return action_name

def get_env_feedback(S, A):
    # This is how agent will interact with the environment
    S1 = cube(S)
    S1.new_state(A)
    S_ = S1.updatestate()
    if S_ in training:
        if training.index(S_) < 17678:
            if S_ == solved:
                R = 1
            else:
                R = 0
        else:
            S_ = S
            R = 0
    else:
        R = 0
        S_ = S

    return S_, R


def update_env(S, episode, step_counter):
    # This is how environment be updated
    b = cube(S)
    if S == solved:
        #print('\r{}'.format(b.updatestate()), end='\r')
        interaction = 'Episode %s: total_steps = %s' % (episode + 1, step_counter)
        print('{}'.format(interaction), end='')
        time.sleep(0.3)
        print('\n')
    else:
        #print('{}'.format(b.updatestate()), end='\r')
        time.sleep(FRESH_TIME)

def rl():
    # main part of RL loop
    global q_table
    q_table = build_q_table(training, ACTIONS)
    for i in range(10089):
        print("state of index : " + str(i+7588))
        for episode in range(MAX_EPISODES):
            step_counter = 0
            S = training[i+7588]
            #print('current state : ', end='')
            #print(S)
            is_terminated = False
            update_env(S, episode, step_counter)
            while not is_terminated:
                actions_taken = []
                A = choose_action(S, q_table)
                S_, R = get_env_feedback(S, A)  # take action & get next state
                #print(A)
                while S == S_:
                    A = choose_action(S, q_table)
                    if not A in actions_taken:
                        actions_taken.append(A)
                        S_, R = get_env_feedback(S, A)
                    else:
                        continue
                # print(A)
                #print(S)
                q_predict = q_table.iloc[training.index(S), q_table.columns.get_loc(A)]
                if S_ != solved:
                    q_target = R + GAMMA * q_table.iloc[training.index(S_), :].max()  # next

                else:
                    q_target = R  # next state is terminal
                    is_terminated = True  # terminate this episode
                q_table.iloc[training.index(S), q_table.columns.get_loc(A)] += ALPHA * (q_target - q_predict)  # update
                S = S_  # move to next state
                if episode == MAX_EPISODES:
                    update_env(S, episode, step_counter + 1)
                step_counter += 1
                #print(q_table)
    return q_table

q_table=rl()
print(q_table)
#build_q_table(training, action)
print('writing to file ....')
q_table.to_csv('q_table_reinforce_4timesshuffle_1.csv', index=False, header=True)
print('done')

#last training was until state of index 9100