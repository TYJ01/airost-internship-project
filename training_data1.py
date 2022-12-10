from cube_enviroment import cube
import numpy as np
import copy
import csv
solved_cube = np.arange(0,54).reshape(1,54)
solved = solved_cube[0].tolist()
training = [solved_cube[0].tolist()]
steps = ["None"]



def train(index, Range):
    global training
    global steps
    for j in range(Range):
        for i in range(12):

            step = copy.deepcopy(steps[index+j])
            a = cube(training[index+j])
            stp = a.train_shuffle(i)
            data = a.updatestate()
            if not data in training:
                training.append(data)
                step.append(stp)
                steps.append(copy.deepcopy(step))
    print('trainings')
    print(len(training) - 1)



for i in range(12):
    step = []
    a = cube(solved_cube)
    stp = a.train_shuffle(i)
    data = a.updatestate()
    if not data in training:
        training.append(data)
        step.append(stp)
    steps.append(step)
print('training')
print(len(training)-1)

'''

for i in range(12):
    for j in range(12):
        a = cube(training[i+1])
        a.train_shuffle(j)
        data = a.updatestate()
        if not data in training :
            training.append(data)
print(len(training)-1)

for i in range(113):
    for j in range(12):
        a = cube(training[i+13])
        a.train_shuffle(j)
        data = a.updatestate()
        if not data in training:
            training.append(data)
print(len(training)-1)
for i in range(1059):
    for j in range(12):
        a = cube(training[i+127])
        a.train_shuffle(j)
        data = a.updatestate()
        if not data in training:
            training.append(data)
print(len(training)-1)
for i in range(9926):
    for j in range(12):
        a = cube(training[i+1187])
        a.train_shuffle(j)
        data = a.updatestate()
        if not data in training:
            training.append(data)
print(len(training)-1)













for sample in training:
    for j in range(12):
        a = cube(sample)
        a.train_shuffle(j)
        data = a.updatestate()
        if not data in training:
            training.append(data)
print('training')
print(len(training))
'''
