"""
A learner for CCG grammars based on the Simulated Annealing algorithm idea
Using the method of MDL for comparisons
"""

import random
import math
import re

from grammars import grammar_pool
from ccg_algorithm import ccg_algorithm


def calculate_MDL(input, grammar):
    """
    calculates the MDL according to a given CCG grammar and an input string
    """
    size = 0
    symbols = set()
    for rule in grammar.values():
        size += len(rule)
        symbols.update(rule)
    g_size = math.ceil(math.log(len(symbols), 2)) * size
    d_given_g_size = math.ceil(math.log(len(grammar_pool), 2)) * len(input)

    MDL = g_size + d_given_g_size
    return MDL


def simulated_annealing(g, t, c):
    """
    The Simulated Annealing algorithm
    """
    assert ccg_algorithm(
        lex = g["lex"],
        const = g["const"],
        max_deg = g["deg"],
        sentence = g["input"]
    )

    while t > 0.01:
        MDL = calculate_MDL(g["input"], g["lex"])
        g_next = random.choice(grammar_pool)
        assert ccg_algorithm(
            lex = g_next["lex"],
            const = g_next["const"],
            max_deg = g_next["deg"],
            sentence = g_next["input"]
        )

        MDL_next = calculate_MDL(g_next["input"],g_next["lex"])
        diff = MDL_next - MDL
        
        if diff < 0:
            p = 1
        else:
            p = math.exp(-diff / t)
        g = random.choices([g_next, g], weights = (p, 1-p), k = 1)[0]
        t = c * t
    return g


def main():
    """
    The main program executes the examle of the input string "abaababaab"
    The returned grammar is the best grammar i.e. the grammar with the lowest MDL score
    In this example this is grammar 3b
    """
    initial_temprature = 100.0
    cooling_factor = 0.999985
    initial_grammar = grammar_pool[0]

    grammar = simulated_annealing(initial_grammar, initial_temprature, cooling_factor)

    print("for input abaababaab, the chosen grammar is: \n")
    print(grammar["lex"])
    

if __name__ == "__main__":
    main()

