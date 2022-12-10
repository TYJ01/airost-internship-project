import numpy as np
import copy
solved_cube = np.arange(0,54).reshape(1,54)

class cube:
    def __init__(self, cubestring):
        self.state = np.array(cubestring).reshape(6,3,3)


    def updatestate(self):
        a = self.state.reshape(1,54)
        b = a[0]
        return b.tolist()


    def cvtstate2str(self):
        cubestring = ''
        for i in range(6):
            for j in range(3):
                for k in range(3):
                    cubestring += str(self.state[i][j][k])
        print(cubestring)
        return cubestring

    def printstate(self):
        print(self.state)

    def up(self, row=0, direction='left'):
        if direction == 'left':
            temp1 = copy.deepcopy(self.state[1][row])
            self.state[1][row],self.state[2][row],self.state[3][row] = self.state[2][row],self.state[3][row],self.state[4][row]
            self.state[4][row] = temp1
            if row == 2 :
                self.state[5]=[list(x) for x in zip(*self.state[5])][::-1]
            if row == 0 :
                self.state[0]=[list(x) for x in zip(*reversed(self.state[0]))]
        if direction == 'right':
            self.state[1][row],self.state[2][row],self.state[3][row],self.state[4][row] = self.state[4][row],self.state[1][row],self.state[2][row],self.state[3][row]
            if row == 2 :
                self.state[5]=[list(x) for x in zip(*reversed(self.state[5]))]
            if row == 0 :
                self.state[0]=[list(x) for x in zip(*self.state[0])][::-1]
        return copy.deepcopy(self.state)

    def up_a(self, row=0, direction='right'):
        if direction == 'left':
            self.state[1][row],self.state[2][row],self.state[3][row],self.state[4][row] = self.state[2][row],self.state[3][row],self.state[4][row],self.state[1][row]
            if row == 2 :
                self.state[5]=[list(x) for x in zip(*self.state[5])][::-1]
            if row == 0 :
                self.state[0]=[list(x) for x in zip(*reversed(self.state[0]))]
        if direction == 'right':
            temp1 = copy.deepcopy(self.state[1][row])
            self.state[1][row],self.state[4][row],self.state[3][row] = self.state[4][row],self.state[3][row],self.state[2][row]
            self.state[2][row] = temp1
            if row == 2 :
                self.state[5]=[list(x) for x in zip(*reversed(self.state[5]))]
            if row == 0 :
                self.state[0]=[list(x) for x in zip(*self.state[0])][::-1]
        return copy.deepcopy(self.state)

    def down(self, row=2, direction='right'):
        if direction == 'left':
            temp1 = copy.deepcopy(self.state[1][row])
            self.state[1][row],self.state[2][row],self.state[3][row] = self.state[2][row],self.state[3][row],self.state[4][row]
            self.state[4][row] = temp1
            if row == 2 :
                self.state[5]=[list(x) for x in zip(*self.state[5])][::-1]
            if row == 0 :
                self.state[0]=[list(x) for x in zip(*reversed(self.state[0]))]
        if direction == 'right':
            temp1 = copy.deepcopy(self.state[1][row])
            self.state[1][row],self.state[4][row],self.state[3][row] = self.state[4][row],self.state[3][row],self.state[2][row]
            self.state[2][row] = temp1
            if row == 2 :
                self.state[5]=[list(x) for x in zip(*reversed(self.state[5]))]
            if row == 0 :
                self.state[0]=[list(x) for x in zip(*self.state[0])][::-1]
        return copy.deepcopy(self.state)

    def down_a(self, row=2, direction='left'):
        if direction == 'left':
            temp1 = copy.deepcopy(self.state[1][row])
            self.state[1][row],self.state[2][row],self.state[3][row] = self.state[2][row],self.state[3][row],self.state[4][row]
            self.state[4][row] = temp1
            if row == 2 :
                self.state[5]=[list(x) for x in zip(*self.state[5])][::-1]
            if row == 0 :
                self.state[0]=[list(x) for x in zip(*reversed(self.state[0]))]
        if direction == 'right':
            temp1 = copy.deepcopy(self.state[1][row])
            self.state[1][row],self.state[4][row],self.state[3][row],self.state[4][row] = self.state[4][row],self.state[3][row],self.state[2][row]
            self.state[2][row] = temp1
            if row == 2 :
                self.state[5]=[list(x) for x in zip(*reversed(self.state[5]))]
            if row == 0 :
                self.state[0]=[list(x) for x in zip(*self.state[0])][::-1]
        return copy.deepcopy(self.state)


    def right(self, column=2, direction='up'):
        if direction == 'up':

            temp0a= self.state[0][0][column]
            temp3a = self.state[3][0][2-column]
            temp0b = self.state[0][1][column]
            temp3b= self.state[3][1][2-column]
            temp0c = self.state[0][2][column]
            temp3c = self.state[3][2][2-column]
            for i in range(3):
                self.state[0][i][column] = self.state[1][i][column]
                self.state[1][i][column] = self.state[5][i][column]
            self.state[3][2][2-column] = temp0a
            self.state[3][1][2-column] = temp0b
            self.state[3][0][2-column] = temp0c
            self.state[5][2][column] = temp3a
            self.state[5][1][column] = temp3b
            self.state[5][0][column] = temp3c
            if column == 0 :
                self.state[4]=[list(x) for x in zip(*self.state[4])][::-1]
            if column == 2 :
                self.state[2] = [list(x) for x in zip(*reversed(self.state[2]))]
        if direction == 'down':
            temp5a= self.state[5][0][column]
            temp3a = self.state[3][0][2-column]
            temp5b = self.state[5][1][column]
            temp3b= self.state[3][1][2-column]
            temp5c = self.state[5][2][column]
            temp3c = self.state[3][2][2-column]
            for i in range(3):
                self.state[5][i][column] = self.state[1][i][column]
                self.state[1][i][column] = self.state[0][i][column]
            self.state[3][2][2-column] = temp5a
            self.state[3][1][2-column] = temp5b
            self.state[3][0][2-column] = temp5c
            self.state[0][2][column] = temp3a
            self.state[0][1][column] = temp3b
            self.state[0][0][column] = temp3c
            if column == 0 :
                self.state[4]= [list(x) for x in zip(*reversed(self.state[4]))]
            if column == 2 :
                self.state[2] = [list(x) for x in zip(*self.state[2])][::-1]
        return copy.deepcopy(self.state)

    def right_a(self, column=2, direction='down'):
        if direction == 'up':

            temp0a= self.state[0][0][column]
            temp3a = self.state[3][0][2-column]
            temp0b = self.state[0][1][column]
            temp3b= self.state[3][1][2-column]
            temp0c = self.state[0][2][column]
            temp3c = self.state[3][2][2-column]
            for i in range(3):
                self.state[0][i][column] = self.state[1][i][column]
                self.state[1][i][column] = self.state[5][i][column]
            self.state[3][2][2-column] = temp0a
            self.state[3][1][2-column] = temp0b
            self.state[3][0][2-column] = temp0c
            self.state[5][2][column] = temp3a
            self.state[5][1][column] = temp3b
            self.state[5][0][column] = temp3c
            if column == 0 :
                self.state[4]=[list(x) for x in zip(*self.state[4])][::-1]
            if column == 2 :
                self.state[2] = [list(x) for x in zip(*reversed(self.state[2]))]
        if direction == 'down':
            temp5a= self.state[5][0][column]
            temp3a = self.state[3][0][2-column]
            temp5b = self.state[5][1][column]
            temp3b= self.state[3][1][2-column]
            temp5c = self.state[5][2][column]
            temp3c = self.state[3][2][2-column]
            for i in range(3):
                self.state[5][i][column] = self.state[1][i][column]
                self.state[1][i][column] = self.state[0][i][column]
            self.state[3][2][2-column] = temp5a
            self.state[3][1][2-column] = temp5b
            self.state[3][0][2-column] = temp5c
            self.state[0][2][column] = temp3a
            self.state[0][1][column] = temp3b
            self.state[0][0][column] = temp3c
            if column == 0 :
                self.state[4]= [list(x) for x in zip(*reversed(self.state[4]))]
            if column == 2 :
                self.state[2] = [list(x) for x in zip(*self.state[2])][::-1]
        return copy.deepcopy(self.state)


    def left(self, column=0, direction='down'):
        if direction == 'up':

            temp0a= self.state[0][0][column]
            temp3a = self.state[3][0][2-column]
            temp0b = self.state[0][1][column]
            temp3b= self.state[3][1][2-column]
            temp0c = self.state[0][2][column]
            temp3c = self.state[3][2][2-column]
            for i in range(3):
                self.state[0][i][column] = self.state[1][i][column]
                self.state[1][i][column] = self.state[5][i][column]
            self.state[3][2][2-column] = temp0a
            self.state[3][1][2-column] = temp0b
            self.state[3][0][2-column] = temp0c
            self.state[5][2][column] = temp3a
            self.state[5][1][column] = temp3b
            self.state[5][0][column] = temp3c
            if column == 0 :
                self.state[4]=[list(x) for x in zip(*self.state[4])][::-1]
            if column == 2 :
                self.state[2] = [list(x) for x in zip(*reversed(self.state[2]))]
        if direction == 'down':
            temp5a= self.state[5][0][column]
            temp3a = self.state[3][0][2-column]
            temp5b = self.state[5][1][column]
            temp3b= self.state[3][1][2-column]
            temp5c = self.state[5][2][column]
            temp3c = self.state[3][2][2-column]
            for i in range(3):
                self.state[5][i][column] = self.state[1][i][column]
                self.state[1][i][column] = self.state[0][i][column]
            self.state[3][2][2-column] = temp5a
            self.state[3][1][2-column] = temp5b
            self.state[3][0][2-column] = temp5c
            self.state[0][2][column] = temp3a
            self.state[0][1][column] = temp3b
            self.state[0][0][column] = temp3c
            if column == 0 :
                self.state[4]= [list(x) for x in zip(*reversed(self.state[4]))]
            if column == 2 :
                self.state[2] = [list(x) for x in zip(*self.state[2])][::-1]
        return copy.deepcopy(self.state)


    def left_a(self, column=0, direction='up'):
        if direction == 'up':

            temp0a= self.state[0][0][column]
            temp3a = self.state[3][0][2-column]
            temp0b = self.state[0][1][column]
            temp3b= self.state[3][1][2-column]
            temp0c = self.state[0][2][column]
            temp3c = self.state[3][2][2-column]
            for i in range(3):
                self.state[0][i][column] = self.state[1][i][column]
                self.state[1][i][column] = self.state[5][i][column]
            self.state[3][2][2-column] = temp0a
            self.state[3][1][2-column] = temp0b
            self.state[3][0][2-column] = temp0c
            self.state[5][2][column] = temp3a
            self.state[5][1][column] = temp3b
            self.state[5][0][column] = temp3c
            if column == 0 :
                self.state[4]=[list(x) for x in zip(*self.state[4])][::-1]
            if column == 2 :
                self.state[2] = [list(x) for x in zip(*reversed(self.state[2]))]
        if direction == 'down':
            temp5a= self.state[5][0][column]
            temp3a = self.state[3][0][2-column]
            temp5b = self.state[5][1][column]
            temp3b= self.state[3][1][2-column]
            temp5c = self.state[5][2][column]
            temp3c = self.state[3][2][2-column]
            for i in range(3):
                self.state[5][i][column] = self.state[1][i][column]
                self.state[1][i][column] = self.state[0][i][column]
            self.state[3][2][2-column] = temp5a
            self.state[3][1][2-column] = temp5b
            self.state[3][0][2-column] = temp5c
            self.state[0][2][column] = temp3a
            self.state[0][1][column] = temp3b
            self.state[0][0][column] = temp3c
            if column == 0 :
                self.state[4]= [list(x) for x in zip(*reversed(self.state[4]))]
            if column == 2 :
                self.state[2] = [list(x) for x in zip(*self.state[2])][::-1]
        return copy.deepcopy(self.state)

    def front(self, column = 0, direction = 'clockwise'):
        if direction == 'clockwise':
            temp4a = self.state[4][0][2-column]
            temp4b = self.state[4][1][2-column]
            temp4c = self.state[4][2][2-column]
            temp5a = self.state[5][column][0]
            temp5b = self.state[5][column][1]
            temp5c = self.state[5][column][2]
            for i in range(3):
                self.state[5][column][i] = self.state[2][2 - i][column]
            temp0a = self.state[0][2][0]
            temp0b = self.state[0][2][1]
            temp0c = self.state[0][2][2]
            self.state[2][0][column] = temp0a
            self.state[2][1][column] = temp0b
            self.state[2][2][column] = temp0c
            self.state[0][2-column][0]=temp4c
            self.state[0][2-column][1]=temp4b
            self.state[0][2-column][2]=temp4a
            self.state[4][0][2-column]=temp5a
            self.state[4][1][2-column]=temp5b
            self.state[4][2][2-column]=temp5c
            if column == 0 :
                self.state[1]=[list(x) for x in zip(*reversed(self.state[1]))]
            if column == 2 :
                self.state[3] = [list(x) for x in zip(*self.state[3])][::-1]

        if direction == 'anticlockwise':
            temp2a = self.state[2][0][column]
            temp2b = self.state[2][1][column]
            temp2c = self.state[2][2][column]
            temp5a = self.state[5][column][0]
            temp5b = self.state[5][column][1]
            temp5c = self.state[5][column][2]
            for i in range(3):
                self.state[5][column][i]=self.state[4][i][2-column]
            temp0a = self.state[0][2][0]
            temp0b = self.state[0][2][1]
            temp0c = self.state[0][2][2]
            self.state[4][0][2] = temp0c
            self.state[4][1][2] = temp0b
            self.state[4][2][2] = temp0a
            self.state[0][2-column][0]=temp2a
            self.state[0][2-column][1]=temp2b
            self.state[0][2-column][2]=temp2c
            self.state[2][0][column]=temp5c
            self.state[2][1][column]=temp5b
            self.state[2][2][column]=temp5a
            if column == 0 :
                self.state[1] = [list(x) for x in zip(*self.state[1])][::-1]
            if column == 2 :
                self.state[3]=[list(x) for x in zip(*reversed(self.state[3]))]
        return copy.deepcopy(self.state)


    def front_a(self, column = 0, direction = 'anticlockwise'):
        if direction == 'clockwise':
            temp4a = self.state[4][0][2-column]
            temp4b = self.state[4][1][2-column]
            temp4c = self.state[4][2][2-column]
            temp5a = self.state[5][column][0]
            temp5b = self.state[5][column][1]
            temp5c = self.state[5][column][2]
            for i in range(3):
                self.state[5][column][i]=self.state[2][2-i][column]
            temp0a = self.state[0][2][0]
            temp0b = self.state[0][2][1]
            temp0c = self.state[0][2][2]
            self.state[2][0][column]= temp0a
            self.state[2][1][column]= temp0b
            self.state[2][2][column]= temp0c
            self.state[0][2-column][0]=temp4c
            self.state[0][2-column][1]=temp4b
            self.state[0][2-column][2]=temp4a
            self.state[4][0][2-column]=temp5a
            self.state[4][1][2-column]=temp5b
            self.state[4][2][2-column]=temp5c
            if column == 0 :
                self.state[1]=[list(x) for x in zip(*reversed(self.state[1]))]
            if column == 2 :
                self.state[3] = [list(x) for x in zip(*self.state[3])][::-1]

        if direction == 'anticlockwise':
            temp2a = self.state[2][0][column]
            temp2b = self.state[2][1][column]
            temp2c = self.state[2][2][column]
            temp5a = self.state[5][column][0]
            temp5b = self.state[5][column][1]
            temp5c = self.state[5][column][2]
            for i in range(3):
                self.state[5][column][i]=self.state[4][i][2-column]
            temp0a = self.state[0][2][0]
            temp0b = self.state[0][2][1]
            temp0c = self.state[0][2][2]
            self.state[4][0][2] = temp0c
            self.state[4][1][2] = temp0b
            self.state[4][2][2] = temp0a
            self.state[0][2-column][0]=temp2a
            self.state[0][2-column][1]=temp2b
            self.state[0][2-column][2]=temp2c
            self.state[2][0][column]=temp5c
            self.state[2][1][column]=temp5b
            self.state[2][2][column]=temp5a
            if column == 0 :
                self.state[1] = [list(x) for x in zip(*self.state[1])][::-1]
            if column == 2 :
                self.state[3]=[list(x) for x in zip(*reversed(self.state[3]))]
        return copy.deepcopy(self.state)


    def back(self, column = 2, direction = 'anticlockwise'):
        if direction == 'clockwise':
            temp4a = self.state[4][0][2-column]
            temp4b = self.state[4][1][2-column]
            temp4c = self.state[4][2][2-column]
            temp5a = self.state[5][column][0]
            temp5b = self.state[5][column][1]
            temp5c = self.state[5][column][2]
            for i in range(3):
                self.state[5][column][i]=self.state[2][2-i][2-column]
            temp0a = self.state[0][0][0]
            temp0b = self.state[0][0][1]
            temp0c = self.state[0][0][2]
            self.state[2][0][2] =temp0a
            self.state[2][1][2] =temp0b
            self.state[2][2][2] =temp0c
            self.state[0][2-column][0]=temp4c
            self.state[0][2-column][1]=temp4b
            self.state[0][2-column][2]=temp4a
            self.state[4][0][2-column]=temp5a
            self.state[4][1][2-column]=temp5b
            self.state[4][2][2-column]=temp5c
            if column == 0 :
                self.state[1]=[list(x) for x in zip(*reversed(self.state[1]))]
            if column == 2 :
                self.state[3] = [list(x) for x in zip(*self.state[3])][::-1]

        if direction == 'anticlockwise':
            temp2a = self.state[2][0][column]
            temp2b = self.state[2][1][column]
            temp2c = self.state[2][2][column]
            temp5a = self.state[5][column][0]
            temp5b = self.state[5][column][1]
            temp5c = self.state[5][column][2]
            for i in range(3):
                self.state[5][column][i]=self.state[4][i][2-column]
                self.state[4][i][2-column]=self.state[0][2-column][2-i]
            self.state[0][2-column][0]=temp2a
            self.state[0][2-column][1]=temp2b
            self.state[0][2-column][2]=temp2c
            self.state[2][0][column]=temp5c
            self.state[2][1][column]=temp5b
            self.state[2][2][column]=temp5a
            if column == 0 :
                self.state[1] = [list(x) for x in zip(*self.state[1])][::-1]
            if column == 2 :
                self.state[3]=[list(x) for x in zip(*reversed(self.state[3]))]
        return copy.deepcopy(self.state)


    def back_a(self, column = 2, direction = 'clockwise'):
        if direction == 'clockwise':
            temp4a = self.state[4][0][2-column]
            temp4b = self.state[4][1][2-column]
            temp4c = self.state[4][2][2-column]
            temp5a = self.state[5][column][0]
            temp5b = self.state[5][column][1]
            temp5c = self.state[5][column][2]
            for i in range(3):
                self.state[5][column][i] = self.state[2][2 - i][column]
            temp0a = self.state[0][0][0]
            temp0b = self.state[0][0][1]
            temp0c = self.state[0][0][2]
            self.state[2][0][2] = temp0a
            self.state[2][1][2] = temp0b
            self.state[2][2][2] = temp0c
            self.state[0][2-column][0]=temp4c
            self.state[0][2-column][1]=temp4b
            self.state[0][2-column][2]=temp4a
            self.state[4][0][2-column]=temp5a
            self.state[4][1][2-column]=temp5b
            self.state[4][2][2-column]=temp5c
            if column == 0 :
                self.state[1]=[list(x) for x in zip(*reversed(self.state[1]))]
            if column == 2 :
                self.state[3] = [list(x) for x in zip(*self.state[3])][::-1]

        if direction == 'anticlockwise':
            temp2a = self.state[2][0][column]
            temp2b = self.state[2][1][column]
            temp2c = self.state[2][2][column]
            temp5a = self.state[5][column][0]
            temp5b = self.state[5][column][1]
            temp5c = self.state[5][column][2]
            for i in range(3):
                self.state[5][column][i]=self.state[4][i][2-column]
                self.state[4][i][2-column]=self.state[0][2-column][2-i]
            self.state[0][2-column][0]=temp2a
            self.state[0][2-column][1]=temp2b
            self.state[0][2-column][2]=temp2c
            self.state[2][0][column]=temp5c
            self.state[2][1][column]=temp5b
            self.state[2][2][column]=temp5a
            if column == 0 :
                self.state[1] = [list(x) for x in zip(*self.state[1])][::-1]
            if column == 2 :
                self.state[3]=[list(x) for x in zip(*reversed(self.state[3]))]
        return copy.deepcopy(self.state)

    def new_state(self, action):
        if action == 'F':
            self.state = self.front()

        if action == "F'":
            self.state = self.front_a()
        if action == 'R':
            self.state = self.right()
        if action == "R'":
            self.state =self.right_a()
        if action == 'B':
            self.state = self.back()
        if action == "B'":
            self.state =self.back_a()
        if action == 'L':
            self.state =self.left()
        if action == "L'":
            self.state =self.left_a()
        if action == 'U':
            self.state =self.up()
        if action == "U'":
            self.state =self.up_a()
        if action == "D":
            self.state =self.down()
        if action == "D'":
            self.state =self.down_a()


    def train_shuffle(self,index):
        list_actions = ["F","F'","R","R'","B","B'","L","L'","U","U'","D","D'"]
        self.new_state(list_actions[index])
        return list_actions[index]


    def shuffle(self, no_times):
        for i in range(12):
            self.train_shuffle(i)

#a = cube(solved_cube)
#a = cube([38, 23, 26, 5, 4, 3, 2, 1, 0, 27, 28, 29, 12, 13, 14, 15, 16, 17, 36, 37, 53, 21, 22, 52, 24, 25, 51, 33, 30, 9, 34, 31, 10, 35, 32, 11, 6, 19, 20, 7, 40, 41, 8, 43, 44, 45, 46, 47, 48, 49, 50, 18, 39, 42])
#a.shuffle(10)
#b= a.updatestate()
#print(b)