"""
Main file for the mini-enterpeter project.

Course: COMP 340
Name: Thomas Rose
"""

import lexer

srcCode = "((12+3*5)+5/4)"
tokSeq = lexer.tokenize(srcCode)

for i in tokSeq:
    print(i[0], i[1])