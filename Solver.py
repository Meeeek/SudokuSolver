# Conrad Fukuzawa

import io
import cell

class SudokuSolver:

    # this is a list of the columns, that way when calling it's x axis first
    elements = [[0, 0, 0, 0, 0, 0, 0, 0, 0],\
                [0, 0, 0, 0, 0, 0, 0, 0, 0],\
                [0, 0, 0, 0, 0, 0, 0, 0, 0],\
                [0, 0, 0, 0, 0, 0, 0, 0, 0],\
                [0, 0, 0, 0, 0, 0, 0, 0, 0],\
                [0, 0, 0, 0, 0, 0, 0, 0, 0],\
                [0, 0, 0, 0, 0, 0, 0, 0, 0],\
                [0, 0, 0, 0, 0, 0, 0, 0, 0],\
                [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    """
    Initializer
    Passed a file containing the puzzle
    """
    def __init__(self, f_path: str):

        file = open(f_path)
        self.is_done = False
        # loops for 3 squares
        for i in range(3):
            # loops for 3 rows
            for j in range(3):
                y_index = 3*i+j
                line = file.readline().split()
                for x_index in range(9):
                    self.elements[x_index][y_index] = line[x_index]
            # readline to get rid of white space
            file.readline()
        # The coordinates are x axis then y axis
        self.curr = [0, 0]


    """
    Move one step in the algorithm
    """
    def step(self):
        cell.Cell currCell = self.elements[self.curr[0]][self.curr[1]]
        
        # if the current cell is valid
        if self.is_valid(currCell): # if the cell is valid, move on
            self.get_next(self.curr)
            if self.curr[1]>8: # this is when we've finished the last cell
                self.is_done = True
        elif currCell.next_num() == -1: # if no valid numbers back track
            self.get_prev(self.curr)
        else:
            currCell.set_num(curCell.next_num())
    
    """
    Prints the puzzle in console
    """
    def visualize(self):
        for i in range(3):
            for j in range(3):
                y_index = i*3 + j
                for x_index in range(9):
                    print(f'{SudokuSolver.elements[x_index][y_index]}', end=' ')
                    if x_index==2 or x_index==5:
                        print("|", end=' ')
                print("")
            if (i!=2):
                print("---------------------")

    """
    Return if finished
    """
    def has_next(self):
        return is_done
        

    def check_valid(cell.Cell c):
        x = c.x_index
        y = c.y_index
        num = c.index+1 # converting to number rather than index
        
        # checking row
        

        # checking column
        

        # checking square
        

    # gets the next coordinate, not bounded on y. coordinate changed in place
    def get_next(coord):
        if(coord[0] == 8):
            coord[0] = 0
            coord[1] += 1
        else:
            coord[0] += 1
        return
    
    # gets the previous coordinate. coordinate changed in place
    def get_prev(coord):
        if(coord[0] == 0):
            coord[0] = 8
            coord[1] -= 1
        else:
            coord[0] -= 1
        return

