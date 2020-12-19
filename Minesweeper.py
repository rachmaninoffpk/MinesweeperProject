'''This is a test version of minesweeper
which will have several layers
v 1.0 October 8, 2020'''



import random




class Board():
    def __init__(self, row = 20, col = 20, dep = 1, mines = 40):
        #x dim is len
        self.row = row
        #y dim is wid
        self.col = col
        #z dim is dep
        self.dep = dep
        self.mines = mines
        self.mineList = []
        self.isRevealed = [[False for i in range(self.col)] for j in range(self.row)]
        self.neighbors = [[None for i in range(self.col)] for j in range(self.row)]
        self.values = [[' ' for i in range(self.col)] for j in range(self.row)]
        self.isLost = False
        self.isWon = False

    def mineGen(self):
        mineList = []
        while(len(mineList) < self.mines):
            x = random.randint(0, self.col-1)
            y = random.randint(0, self.row-1)
            if self.dep is not None:
                z = random.randint(0, self.dep - 1)
                temp = [x,y,z]
            else:
                temp = [x,y]
            if temp not in mineList:
                    mineList.append(temp)
        self.mineList = mineList

    def isMine(self, x, y, z = None):
        if not z:
            if [x,y] in self.mineList:
                return 1
        else:
            if [x,y,z] in self.mineList:
                return 1
        return 0

    def countNeighbors(self, row, col):
        count = 0
        if row == 0:
            if (col == 0):
                count = self.isMine(0,1) + self.isMine(1,0) + self.isMine(1,1)
            elif col == (self.col - 1):
                count = self.isMine(0, self.col - 2) + self.isMine(1,self.col - 2) + self.isMine(1, self.col - 1)
            else:
                count = self.isMine(0, col-1)+ self.isMine(1, col-1) + self.isMine(1, col) + self.isMine(1, col+1) + self.isMine(0, col+1)
        elif row == (self.row - 1):
            if (col == 0):
                count = self.isMine(row,1) + self.isMine(row-1,0) + self.isMine(row - 1,1)
            elif col == (self.col - 1):
                count = self.isMine(row, self.col - 2) + self.isMine(row-1,self.col - 2) + self.isMine(row-1, self.col - 1)
            else:
                count = self.isMine(row, col-1)+ self.isMine(row-1, col-1) + self.isMine(row-1, col) + self.isMine(row-1, col+1)+ self.isMine(row, col+1)
        elif col == 0:
            count = self.isMine(row-1, 0) + self.isMine(row-1, 1) + self.isMine(row, 1) + self.isMine(row+1, 1) + self.isMine(row+1, 0)
        elif col == (self.col - 1):
            count = self.isMine(row-1, col) + self.isMine(row-1, col-1) + self.isMine(row, col-1) + self.isMine(row+1, col-1) + self.isMine(row+1, col)
        else:
            count = self.isMine(row-1, col-1) + self.isMine(row-1, col) + self.isMine(row-1, col+1) + self.isMine(row, col-1) + self.isMine(row, col+1) + self.isMine(row+1, col-1) + self.isMine(row+1, col) + self.isMine(row+1, col+1)
        return count
    
    def getMines(self):
        print(self.mineList)

    def genNeighbors(self):
        for i in range(self.row):
            for j in range(self.col):
                print('i {} and j {}'.format(i,j))
                self.neighbors[i][j] = self.countNeighbors(i,j)
                if self.isMine(i,j) == 1:
                    self.values[i][j] = -1
            print(self.values[i])
        
                

    def getNeighbors(self, row, col):
        count = []
        if row == 0:
            if (col == 0):
                count = [[0,1],[1,0],[1,1]]
            elif col == (self.col - 1):
                count = [[0, self.col - 2], [1,self.col - 2], [1, self.col - 1]]
            else:
                count = [[0, col-1],[1, col-1],[1, col],[1, col+1],[0, col+1]]
        elif row == (self.row - 1):
            if (col == 0):
                count = [[row,1],[row-1,0],[row - 1,1]]
            elif col == (self.col - 1):
                count = [[row, self.col - 2],[row-1,self.col - 2],[row-1, self.col - 1]]
            else:
                count = [[row, col-1],[row-1, col-1],[row-1, col],[row-1, col+1],[row, col+1]]
        elif col == 0:
            count = [[row-1, 0],[row-1, 1],[row, 1],[row+1, 1],[row+1, 0]]
        elif col == (self.col - 1):
            count = [[row-1, col],[row-1, col-1],[row, col-1],[row+1, col-1],[row+1, col]]
        else:
            count = [[row-1, col-1],[row-1, col],[row-1, col+1],[row, col-1],[row, col+1],[row+1, col-1],[row+1, col],[row+1, col+1]]
        return count

    #Fix Flood Fill!!!
    def fillNeighbors(self, row, col):
        neighborlist = []
        neighborlist.append([row, col])
        while(True):
            print(neighborlist)
            now = neighborlist.pop(0)
            i, j = now[0], now[1]
            if self.isRevealed[i][j]:
                temp = self.getNeighbors(i,j)
                print(temp)
                for k in range(len(temp)):
                    r, c = temp[k][0], temp[k][1]
                    if self.isMine(r,c):
                        continue
                    else:
                        if (self.neighbors[r][c] == 0) and (not self.isRevealed[r][c]):
                            neighborlist.append([r,c])
                            self.isRevealed[r][c] = True
                            self.values[r][c] = 0
                            print('[{},{}] is now revealed'.format(r,c))
                        elif (self.neighbors[r][c] == 0) and (self.isRevealed[r][c]):
                            print('[{},{}] is already revealed'.format(r,c))
                        elif self.neighbors[r][c] > 0:
                            self.isRevealed[r][c] = True
                            self.values[r][c] = self.neighbors[r][c]
            if len(neighborlist) == 0:
                break
        for i in range(self.row):
            temp = []
            for j in range(self.col):
                if self.isRevealed[i][j]:
                    temp.append('R')
                else:
                    temp.append('H')
            print(temp)
                


    def reveal(self, row, col, isFlag=False):
        if isFlag:
            print('Flagging')
            if self.values[row][col] == 'F':
                print('Remove flag')
                self.values[row][col] = ''
                self.isRevealed[row][col] = False
                print(self.values[row][col])
            else:
                print('Place flag')
                self.isRevealed[row][col] = True
                self.values[row][col] = 'F'
        else:
            if self.isMine(row, col):
                self.isLost = True
                for i in range(self.row):
                    for j in range(self.col):
                        self.isRevealed[i][j] = True
                        if self.isMine(i,j):
                            self.values[i][j] = 'B'
                        else:
                            self.values[i][j] = self.neighbors[i][j]
                print('bomb')
            else:
                self.isRevealed[row][col] = True
                if self.countNeighbors(row,col) == 0:
                    self.fillNeighbors(row, col)
                self.values[row][col] = self.neighbors[row][col]
                print('Done')
    
    def flag(self, row, col):
        print('Flag')
        self.reveal(row, col, True)

    def press(self, row, col):
        self.reveal(row, col)
    
    def display(self):
        counter = 0
        for i in range(len(self.values)):
            temp = []
            for j in range(len(self.values[i])):
                if self.isRevealed[i][j]:
                    counter += 1
                    temp.append(self.values[i][j])
                else:
                    temp.append('')
            print(temp)
        print(counter)

    
    def nextMove(self):
        while(True):
            row = input('Input row number\n')
            try:
                row = int(row)
            except:
                print('Input a correct value')
            if  isinstance(row, int):
                if (row < 0) or (row >= self.row):
                    print('Input a correct value')
                else:
                    break
        while(True):
            col = input('Input col number\n')
            try:
                col = int(col)
            except:
                print('Input a correct value')
            if  isinstance(col, int):
                if (col < 0) or (col >= self.col):
                    print('Input a correct value')
                else:
                    break
        guess = input('Flag or press? (F or P)\n')
        if guess == 'F':
            self.flag(row, col)
        elif guess == 'P':
            self.press(row, col)
        self.display()

                


def runProgram():
    '''
    while(True):
        rows = input('Please input the number of rows you want to play, between 20 and 40.\n')
        try:
            rows = int(rows)
        except:
            print('Please input a valid response!\n')
        if isinstance(rows, int):
            if 20 <= rows <= 40:
                break
            else:
                print('Please input an integer in the correct range!\n')
    while(True):
        cols = input('Please input the number of columns you want to play, between 20 and 40.\n')
        try:
            cols = int(cols)
        except:
            print('Please input a valid response!\n')
        if isinstance(cols, int):
            if 20 <= cols <= 40:
                break
            else:
                print('Please input an integer in the correct range!\n')
        #else:
        #    print('Please input a valid response!\n')
    while(True):
        mines = input('Please input the number of mines you want to play, between 40 and {}.\n'.format(rows*cols))
        try:
            mines = int(mines)
        except:
            print('Please input a valid response!\n')
        if isinstance(mines, int):
            if 40 <= mines <= rows*cols:
                break
            else:
                print('Please input an integer in the correct range!\n')
        
    print('The board consists of {} rows and {} columns, with {} mines!'.format(rows, cols, mines))
    
    board = Board(rows, cols, None, mines)'''
    board = Board(20,20, None, 40)
    board.mineGen()
    board.genNeighbors()
    board.getMines()
    while(not (board.isLost or board.isWon)):
        board.nextMove()
    if board.isLost:
        print('You have lost!!!')
    elif board.isWon:
        print('You have won!!!')
    
    
        


def promptProgram():
    playing = True
    while(playing):
        response = input('Would you like to play a game of minesweeper? (Y or N)\n')
        if response == 'Y':
            runProgram()
            print('Yay')
            playing = False
        elif response == 'N':
            print('Boo')
            playing = False
        else:
            print('Please input either "Y" for yes or "N" for no!\n')



promptProgram()