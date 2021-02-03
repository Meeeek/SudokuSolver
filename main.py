# Conrad Fukuzawa
# Sudoku Solver visualizer
import Solver
import Visualizer

def main():

    path = "Puzzle.txt"
    py_s = Solver.SudokuSolver(path)
    v = Visualizer.Visualizer(py_s.cells)   

    while(py_s.has_next()):
        py_s.step()
        v.draw()

    while(True):
        v.draw()

    print(py_s.steps)
    

if __name__ == "__main__":
    main()