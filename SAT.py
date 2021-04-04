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
    
This script: Creates the SAT class (short for propositional logic satisfiability
    problem), implements the GSAT and WALKSAT algorithms, and ouput
    the variable assignments to a solution file '.sol' if needed.

"""

from display import display_sudoku_solution
import random

class SAT:
    def __init__(self, filename):
        with open(filename) as f:
            self.clauses = [line.split() for line in f]
        self.vars = []
        for clause in self.clauses:
            for literal in clause:
                if literal[0] != "-":
                    if literal not in self.vars:
                        self.vars.append(literal)
                else:
                    if literal[1:4] not in self.vars:
                        self.vars.append(literal[1:4])
        self.num_vars = len(self.vars)
        self.num_clauses = len(self.clauses)
        self.assignment = []
        self.flips = 0


    def gsat(self):
        """Returns the correct value assignments if found. """
        
        h = 0.7
        self.assignment = [random.choice([1, 0]) for i in range(self.num_vars)]
        while True:
            self.flips += 1
            satisfied, num_satisfaction, false_clause_indices = self.model_satisfies_clauses()
            if satisfied:
                print("Number of flips: " + str(self.flips))
                return True
            if random.random() > h:
                var_index = random.randrange(0, self.num_vars)
            else:
                highest_score_vars = self.evaluate_gsat()
                var_index = random.choice(highest_score_vars)
            self.assignment[var_index] = int(not self.assignment[var_index])

            
    def variable_index(self, literal):
        """Returns the index of the variable in the literal according to its
        position in self.vars"""
        
        if literal[0] == "-":
            r, c, v = int(literal[1]), int(literal[2]), int(literal[3])
        else:
            r, c, v = int(literal[0]), int(literal[1]), int(literal[2])
        index = (r - 1) * 81 + (c - 1) * 9 + v - 1
        return index


    def literal_value(self, literal):
        """Returns the value of the literal in the current assignment"""
        
        var_index = self.variable_index(literal)
        var_value = self.assignment[var_index]
        if literal[0] == "-":
            literal_value = int(not var_value)
        else:
            literal_value = var_value
        return literal_value
    
    
    def model_satisfies_clauses(self):
        """Returns:
               satisfied - True if the current assignment satisfies all the clauses
               num_satisfaction - int, the number of clauses satisfied by the current assignment
               false_clause_indices - list of ints, a list of indices of the clauses
                                       not satisfied by the current assignment
        """

        num_satisfaction = 0
        false_clause_indices = []
        satisfied = True
        for i in range(self.num_clauses):
            for literal in self.clauses[i]:
                literal_val = self.literal_value(literal)
                if literal_val == 1:
                    num_satisfaction += 1
                    break
            else:
                false_clause_indices.append(i)
                satisfied = False
        return satisfied, num_satisfaction, false_clause_indices
    
    
    def evaluate_gsat(self):
        """Scores for each variable how many clauses would be satisfied if the
        variable value were flipped. Returns a list of variables indices with 
        the highest score."""
        
        highest_score = 0
        highest_score_vars = []
        for i in range(self.num_vars):
            self.assignment[i] = int(not self.assignment[i])
            score = self.model_satisfies_clauses()[1]
            if score > highest_score:
                highest_score = score
                highest_score_vars = [i]
            elif score == highest_score:
                highest_score_vars.append(i)
            self.assignment[i] = int(not self.assignment[i])
        return highest_score_vars


    def walksat(self):
        """Returns the correct value assignments if found. """

        p = 0.3
        q = 0.1
        max_flips = 100000
        self.assignment = [random.choice([1, 0]) for i in range(self.num_vars)]
        
        for i in range(max_flips):
            self.flips += 1          
            satisfied, num_satisfaction, false_clause_indices = self.model_satisfies_clauses()
            if satisfied:
                print("Number of flips: " + str(self.flips))
                return True
            
            # if the number of unsatisfied clauses is equal or smaller than 2,
            # then chooses a random variable from the entire set of variables
            if num_satisfaction >= self.num_clauses - 2 and random.random() < q:
                var_index = random.randrange(0, self.num_vars)
            else:
                clause_index = random.choice(false_clause_indices)
                clause = self.clauses[clause_index]
                if random.random() < p:
                    var = random.choice(clause)
                else:
                    highest_score_vars = self.evaluate_walksat(clause)
                    var = random.choice(highest_score_vars)
                var_index = self.variable_index(var)             
            self.assignment[var_index] = int(not self.assignment[var_index])
            
        return False


    def evaluate_walksat(self, clause):
        """ Scores for each variable in the given clause how many clauses would
        be satisfied if the variable value were flipped. Returns a list of 
        variables indices with the highest score."""
        
        highest_score = 0
        highest_score_vars = []
        for var in clause:
            var_index = self.variable_index(var)
            self.assignment[var_index] = int(not self.assignment[var_index])
            score = self.model_satisfies_clauses()[1]
            if score > highest_score:
                highest_score = score
                highest_score_vars = [var]
            elif score == highest_score:
                highest_score_vars.append(var)
            self.assignment[var_index] = int(not self.assignment[var_index])
        return highest_score_vars
    
    
    def write_solution(self, filename):
        """Outputs the current value assignments to a file with the given filename"""

        with open(filename, 'w') as f:
            for i in range(len(self.assignment)):
                if self.assignment[i] == 1:
                    f.write(self.vars[i] + "\n")
                else:
                    f.write("-" + self.vars[i] + "\n")


    def display_solution(self, filename):
        """Displays the sudoku problem based on the solution in the file"""

        display_sudoku_solution(filename)




