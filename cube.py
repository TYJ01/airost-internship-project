perfect_cube = []

for i in range(0,6):
    perfect_cube.append([])
    for j in range(0,3):
        perfect_cube[i].append([])
        for k in range(0,3):
            perfect_cube[i][j].append([i,j,k])

#print(perfect_cube)

class cube:
    def __init__(self, state):
        self.initialstate = state
        self.currentstate = state

    def printstate(self):
        print(self.currentstate)

    # 3 types of moves (each moves turns only 90 degrees)
    def horizontal_twist(self, row, direction):
        if direction == 'left':
            self.currentstate[1][row],self.currentstate[2][row],self.currentstate[3][row],self.currentstate[4][row] = self.currentstate[2][row],self.currentstate[3][row],self.currentstate[4][row],self.currentstate[1][row]
            if row == 2 :
                self.currentstate[5]=[list(x) for x in zip(*self.currentstate[5])][::-1]
            if row == 0 :
                self.currentstate[0]=[list(x) for x in zip(*reversed(self.currentstate[0]))]
        if direction == 'right':
            self.currentstate[1][row],self.currentstate[2][row],self.currentstate[3][row],self.currentstate[4][row] = self.currentstate[4][row],self.currentstate[1][row],self.currentstate[2][row],self.currentstate[3][row]
            if row == 2 :
                self.currentstate[5]=[list(x) for x in zip(*reversed(self.currentstate[5]))]
            if row == 0 :
                self.currentstate[0]=[list(x) for x in zip(*self.currentstate[0])][::-1]

    def vertical_twist(self, column, direction):
        if direction == 'up':
            for i in range(3):
                self.currentstate[1][i][column]=self.currentstate[5][i][column]
                self.currentstate[0][i][column]=self.currentstate[1][i][column]
                self.currentstate[3][2-i][column]=self.currentstate[0][i][column]
                self.currentstate[5][2-i][column]=self.currentstate[3][i][column]
            if column == 0 :
                self.currentstate[4]=[list(x) for x in zip(*self.currentstate[4])][::-1]
            if column == 2 :
                self.currentstate[2] = [list(x) for x in zip(*reversed(self.currentstate[2]))]
        if direction == 'down':
            for i in range(3):
                self.currentstate[1][i][column]=self.currentstate[0][i][column]
                self.currentstate[5][i][column]=self.currentstate[1][i][column]
                self.currentstate[3][2-i][column]=self.currentstate[5][i][column]
                self.currentstate[0][2-i][column]=self.currentstate[3][i][column]
            if column == 0 :
                self.currentstate[4]= [list(x) for x in zip(*reversed(self.currentstate[4]))]
            if column == 2 :
                self.currentstate[2] = [list(x) for x in zip(*self.currentstate[2])][::-1]

    def side_twist(self, column, direction):
        if direction == 'clockwise':
           for i in range(3):
                self.currentstate[2][i][column]=self.currentstate[0][2-column][i]
                self.currentstate[4][i][2-column]=self.currentstate[5][column][i]
           for i in range(3):
                self.currentstate[0][2-column][i]= self.currentstate[4][i][2-column]
                self.currentstate[5][column][i]=self.currentstate[2][column][2-i]
           if column == 0 :
                self.currentstate[1]=[list(x) for x in zip(*reversed(self.currentstate[1]))]
           if column == 2 :
                self.currentstate[3] = [list(x) for x in zip(*self.currentstate[3])][::-1]

        if direction == 'anticlockwise':
            for i in range(3):
                self.currentstate[4][i][2-column]=self.currentstate[0][2-column][2-i]
                self.currentstate[2][i][column]=self.currentstate[5][column][2-i]
            for i in range(3):
                self.currentstate[0][2-column][i]= self.currentstate[2][i][column]
                self.currentstate[5][column][i]=self.currentstate[4][i][2-column]
            if column == 0 :
                self.currentstate[1] = [list(x) for x in zip(*self.currentstate[1])][::-1]
            if column == 2 :
                self.currentstate[3]=[list(x) for x in zip(*reversed(self.currentstate[3]))]


a = cube(perfect_cube)
a.printstate()
a.side_twist(2, 'clockwise')
a.printstate()