"""
Author: Zitong Wu
Date: Oct 26, 2020

Description:
    Writes a general-purpose solver with GSAT and WALKSAT algorithms
    for propositional logic satisfiability problems. To test the solver, 
    sudoku logic puzzles are turned into conjunctive normal forms (CNF)
    and are thus modeled as satisfiability problems. Note that sudoku
    puzzles are used as an example here. GSAT and WALKSAT algorithms 
    can be applied to other satisfiability problems as well. 
    
This script: Display a *.sol solution file that lists the name of every 
variable in the assignment, with either no sign for a true value, 
or a negative sign for a false value (provided code).

"""
from Sudoku import Sudoku
import sys

def display_sudoku_solution(filename):

    test_sudoku = Sudoku()
    test_sudoku.read_solution(filename)
    print(test_sudoku)

if __name__ == "__main__":
    display_sudoku_solution(sys.argv[1])