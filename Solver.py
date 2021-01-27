# Conrad Fukuzawa

import io
import cell
import time

class SudokuSolver:

    # this is a list of the columns, that way when calling it's x axis first
    # the numbers are placeholders, the actual list is a list of Cell objects
    cells = []
    origin_pts = []

    """
    Initializer
    Passed a file containing the puzzle
    """
    def __init__(self, f_path: str):
        self.steps = 0
        file = open(f_path)

        # this adds 9 empty lists, they are the 9 y axis's
        for i in range(9):
            self.cells.append([])

        # loops for 3 squares
        for i in range(3):
            # loops for 3 rows
            for j in range(3):
                y_index = 3*i+j
                line = file.readline().split()
                for x_index in range(9):
                    num = int(line[x_index])
                    self.cells[y_index].append(cell.Cell(num, x_index, y_index))
                        # This passes in the num, x_index, and y_index
                    if num != 0:
                        self.origin_pts.append((x_index, y_index))
            # readline to get rid of white space
            file.readline()
        # The coordinates are x axis then y axis
        self.curr = [0, 0]


    """
    Move one step in the algorithm
    """
    def step(self):
        # this is of type Cell
        self.steps += 1
        currCell = self.cells[self.curr[1]][self.curr[0]]
        
        while currCell.is_fixed:
            self.get_next(self.curr)
            currCell = self.cells[self.curr[1]][self.curr[0]]

        print(self.curr)
        # if the current cell is valid
        if self.is_valid(currCell): # if the cell is valid, move on
            self.get_next(self.curr) # moves coordinates to next position
        elif currCell.next_num() == -1: # if no valid numbers back track
            #print("backtrack")
            currCell.set_num(0)
            currCell.reset_i()
            self.get_prev(self.curr) # moves coordinates to previous position
            prevCell = self.cells[self.curr[1]][self.curr[0]]
            while prevCell.is_fixed:
                self.get_prev(self.curr)
                prevCell = self.cells[self.curr[1]][self.curr[0]]

            # this removes the number so that it knows this number is not valid
            prevCell = self.cells[self.curr[1]][self.curr[0]]
            prevCell.remove_num(self.cells[self.curr[1]][self.curr[0]].get_num())
            prevCell.set_num(0)
            
        else:
            currCell.set_num(currCell.next_num())
        #time.sleep(0.5)
    
    """
    Prints the puzzle in console
    """
    def visualize(self):
        for i in range(3):
            for j in range(3):
                y_index = i*3 + j
                for x_index in range(9):
                    print(f'{self.cells[y_index][x_index].get_num()}', end=' ')
                    if x_index==2 or x_index==5:
                        print("|", end=' ')
                print("")
            if (i!=2):
                print("---------------------")

    """
    Return if finished
    """
    def has_next(self):
        return self.curr[0] < 9 and self.curr[1] < 9
        

    def is_valid(self, c: cell.Cell):
        x = c.x
        y = c.y
        num = c.num
        
        if num == 0:
            return False
        
        # checking row
        for x_i in range(9):
            if (x_i != x) and (self.cells[y][x_i].get_num() == num):
                return False

        # checking column
        for y_i in range(9):
            if (y_i != y) and (self.cells[y_i][x].get_num() == num):
                return False

        # checking square
        # first step find quadrant
        top_left = ((x//3) * 3, (y//3) * 3)
        print(f"top_left: {top_left}")
        # second step interate through indexes
        for x_i in range(top_left[0], top_left[0]+3):
            for y_i in range(top_left[1], top_left[1]+3):
                if not(x_i==x and y_i==y) and (self.cells[y_i][x_i].get_num() == num):
                    return False
        return True

    # gets the next coordinate, not bounded on y. coordinate changed in place
    def get_next(self, coord):
        if(coord[0] == 8):
            coord[0] = 0
            coord[1] += 1
        else:
            coord[0] += 1
        return
    
    # gets the previous coordinate. coordinate changed in place
    def get_prev(self, coord):
        if(coord[0] == 0):
            coord[0] = 8
            coord[1] -= 1
        else:
            coord[0] -= 1
        return

