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
    
This script: Implements a utility that lets you do the sud to cnf
conversion from the command-line (provided code)

"""

from Sudoku import Sudoku
import sys

if __name__ == "__main__":
    test_sudoku = Sudoku()

    test_sudoku.load(sys.argv[1])
    print(test_sudoku)

    puzzle_name = sys.argv[1][:-4]
    cnf_filename = puzzle_name + ".cnf"

    test_sudoku.generate_cnf(cnf_filename)
    print("Output file: " + cnf_filename)

