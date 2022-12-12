from cube_reconigtion import detect_cube
from conversion import cvt2kociemba
import kociemba
from conversion import cvt2env
from cube_stepsdisplay import display, steps_converter
import csv

def kociemba_solve():
    global solution
    cube_state = detect_cube()
    cube = cvt2kociemba(cube_state)
    solution = str(kociemba.solve(cube))
    print(kociemba.solve(cube))
    solution1 = steps_converter(solution)
    print(solution1)
    display(solution1)
    return solution

def reinforce_solve():
    global solution
    cube_state = detect_cube()
    cube = cvt2env(cube_state)
    print(cube)
    with open('training_set6.csv', 'r') as f:
        reader = csv.reader(f)
        training = [[int(element) for element in row] for row in reader]
    with open('6solvesteps.csv', 'r') as f:
        reader = csv.reader(f)
        solvedstep = [row for row in reader]
    cube1 = cube.reshape(1, 54)
    cube1 = cube1.tolist()
    cube2 = cube1[0]
    print(cube1)
    print(cube2)
    if cube2 in training:
        solution = solvedstep[training.index(cube2)]
        print(training.index(cube2))
    display(solution)


kociemba_solve()


#cube_state = detect_cube()

#cube = cvt2env([[['B', 'B', 'B'], ['G', 'B', 'B'], ['B', 'B', 'B']], [['W', 'W', 'Y'], ['W', 'W', 'Y'], ['W', 'W', 'Y']], [['O', 'R', 'R'], ['O', 'R', 'R'], ['O', 'R', 'R']], [['Y', 'Y', 'W'], ['Y', 'Y', 'W'], ['Y', 'Y', 'W']], [['R', 'O', 'O'], ['R', 'O', 'O'], ['R', 'O', 'O']], [['G', 'G', 'G'], ['B', 'G', 'G'], ['G', 'G', 'G']]])
#print(cube)

#solution = "U L' U2 F2 B' R' U' F2 U' B U2 D F2 L2 U2 B2 L2 U2 F2 U'"
#solution1 = steps_converter(solution)
#print(solution1)
#display(solution1)