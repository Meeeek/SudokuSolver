# Conrad Fukuzawa

import io

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

        # loops for 3 squares
        for i in range(3):
            # loops for 3 rows
            for j in range(3):
                y_index = 3*i+j
                line = file.readline().split()
                for x_index in range(9):
                    SudokuSolver.elements[x_index][y_index] = line[x_index]
            # readline to get rid of white space
            file.readline()
        # The coordinates are x axis then y axis


    """
    Move one step in the algorithm
    """
    def step(self):
        pass
    
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
        return False

