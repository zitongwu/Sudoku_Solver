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
    
This script: Implements the main program of the sudoku solver (provided code)

"""

from display import display_sudoku_solution
import random, sys
from SAT import SAT

if __name__ == "__main__":
    # for testing, always initialize the pseudorandom number generator to output the same sequence
    #  of values:
    random.seed(1)

    puzzle_name = str(sys.argv[1][:-4])
    sol_filename = puzzle_name + ".sol"

    sat = SAT(sys.argv[1])

    result = sat.gsat()

    if result:
        sat.write_solution(sol_filename)
        display_sudoku_solution(sol_filename)