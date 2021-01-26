# Conrad Fukuzawa

import io

class SudokuSolver:

    elements = [[]]

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
                y_index = i+j
                line = file.readline().split()
                for x_index in range(10):
                    elements[x_index][y_index] = line[x_index]
            # readline to get rid of white space
            file.readline()


    """
    Move one step in the algorithm
    """
    def step(self):
        pass
    
    """
    Return list of rows
    """
    def visualize(self):
        pass

    """
    Return if finished
    """
    def has_next(self):
        return False

