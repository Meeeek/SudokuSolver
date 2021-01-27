# Conrad Fukuzawa
# Sudoku Solver visualizer
import Solver

def main():

    path = "Puzzle.txt"
    py_s = Solver.SudokuSolver(path)
    py_s.visualize()

    while(py_s.has_next()):
        py_s.step()
        #py_s.visualize()
    print(py_s.steps)
    py_s.visualize()

def draw(input: str):
    pass


if __name__ == "__main__":
    main()