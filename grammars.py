"""
This file contains the pool of grammars for the example
each grammar has the input inialized according to it's corresponding rules
The grammars are such that can parse the input with the CCG parsing algorithm
"""

G1 = {
    "input" : "a1 b1 a1 a1 b1 a2 b2 a2 a2 b3",
    "lex" : {
        "a1" : r'A',
        "a2" : r'S\A/S',
        "a3" : r'S\A',
        "b1" : r'B',
        "b2" : r'S\B/S',
        "b3" : r'S\B'
    },
    "const" : 3,
    "deg"   : 1
}


G2 = {
    "input" : "ab1 aa2 ba1 ba2 ab3",
    "lex" : {
        "ab1" : r'A',
        "ab2" : r'S/A\A',
        "ab3" : r'B\A',
        "ba1" : r'B',
        "ba2" : r'S/B\B',
        "ba3" : r'A\B',
        "aa1" : r'A/A',
        "aa2" : r'A\A',
        "aa3" : r'B/B',
        "aa4" : r'B\B'
    },
    "const" : 3,
    "deg" : 1
}


G3 = {
    "input" : "aba1 aba2 baab1",
    "lex" : {
        "aba1" : r'A',
        "aba2" : r'S\A/B',
        "baab1" : r'B',
        "baab2" : r'B/B'
    },
    "const" : 3,
    "deg" : 1
}

G3b =  {
    "input" : "aba1 aba2 baab1",
    "lex" : {
        "aba1" : r'A',
        "aba2" : r'S\A/B',
        "baab1" : r'B',
    },
    "const" : 3,
    "deg" : 1
}

grammar_pool = [G1, G2, G3, G3b]