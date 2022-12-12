import csv
import copy

with open('6shufflesteps.csv', 'r') as f:
    reader = csv.reader(f)
    result =[ row for row in reader]
    training = result

solvestep = []
for shuffle in training:
    print(shuffle)
    temp = shuffle
    temp.reverse()
    for step in temp:
        if step == "F":
            temp[temp.index(step)] = "F'"
        if step == "F'":
            temp[temp.index(step)] = "F"
        if step == "R":
            temp[temp.index(step)] = "R'"
        if step == "R'":
            temp[temp.index(step)] = "R"
        if step == "L":
            temp[temp.index(step)] = "l'"
        if step == "L'":
            temp[temp.index(step)] = "L"
        if step == "B":
            temp[temp.index(step)] = "B'"
        if step == "B'":
            temp[temp.index(step)] = "B"
        if step == "U":
            temp[temp.index(step)] = "U'"
        if step == "U'":
            temp[temp.index(step)] = "U"
        if step == "D":
            temp[temp.index(step)] = "D'"
        if step == "D'":
            temp[temp.index(step)] = "D"
    solvestep.append(temp)
    print(temp)

with open('6solvesteps.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(solvestep)