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
    
This script: Lets you specify a sudoku cnf filename, solves the sudoku,
saves and displays the solution

"""

from SAT import SAT
import time

filename = "puzzle2.cnf"
puzzle_name = filename[0:-4]
solution_filename = puzzle_name + ".sol"
sat = SAT(filename)
print(sat.vars)
start = time.time()
sat.walksat()
end = time.time()
print("Time: " + str(end-start))
sat.write_solution(solution_filename)
sat.display_solution(solution_filename)