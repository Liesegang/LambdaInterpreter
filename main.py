#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lexer import Lexer
from parser import Parser, ParserError
from visitors import BetaReduction

def interpret(source, print_reductions=False):
    try:
        l = Lexer(source)
        ast = Parser(l).parse()
    except ParserError as discrepancy:
        print('ParserError: ' + discrepancy.message)
    normal_form = False
    while not normal_form:
        reducer = BetaReduction()
        reduced_ast = reducer.visit(ast)
        normal_form = not reducer.reduced
        if print_reductions:
            print(ast)
        ast = reduced_ast
    return str(ast)


def main():
    """Begin an interactive lambda calculus interpreter"""
    print("lambda calculation")
    print("'quit' to exit.")

    while True:
        read = input('> ')
        if read == 'quit':
            break
        if read != '':
            interpret(read, print_reductions = True)

if __name__ == '__main__':
    main()
