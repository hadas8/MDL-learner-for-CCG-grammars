# MDL-learner-of-CCG-grammars-for-mildly-context-sensitive-languages

A Python implementation of an algorithmic MDL learner for CCG grammars, using the method of MDL learning and a Simulated Annealing algorithm.
This project is my submission for Learning: Computation and Cognition Seminar in the computational linguistics program in Tel Aviv University.

## Description

Avraham (2017) has stated in his work on head-complement order learner that to implement a syntactic grammar, several models are required:
-	Formalism – a description of the grammar.
-	Parser – an algorithm that tests whether a given grammar generates the input sentence.
-	Metric – a method to compare different grammars in order to choose the "best" one.
-	Learning algorithm.
I have chosen the formalism of CCG that can represent a mildly context sensitive grammar and have already created a parser that is able to recognize sentences given a CCG grammar.
The next step, according to Avraham, is to select a metric for comparing the grammars. This metric is the Minimum Description Length. 

For addiditonal information about CCG grammarms, the parsing algorithm, the simualted annealing algorithm and the MDL method, A PDF file describing my project is attached, along with the references and source material.


## Implementation Details

The Algorithm receives an input string and an initial grammar and in each iteration the algorithm generates a random grammar and validates the parsing of the input by this grammar. It then calculates the MDL and compares it to the previous to select the new grammar according to the probability function presented above (in the pseudo code).
Following Rasin and Katzir (2016), I have selected the initial temperature to be 100.0 and the cooing factor α to be 0.999985.

I implemented several methods in 2 Python files:
Simulated algorithm learner:
	The simulated annealing algorithm as described above
	MDL calculation method for calculating MDL of a given grammar in CCG and input string
	A main program that tests the algorithm, with the examples detailed below
Grammars:
	a grammar pool – a collection of CCG grammars compatible with the examples detailed below
Additionally, submitted with this work are 3 more Pthon files:
	ccg_algorithm
	rules
	lexicon
These files are the implementation of the CCG parser I used, that Ihave implemented in my previous work.

