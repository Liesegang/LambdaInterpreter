#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lexer import Lexer
from parser import Parser, ParserError

if __name__ == '__main__':
    # write your code here
    while True:
        source = input('>')
        if source == 'q':
            break
        try:
            l = Lexer(source)
            p = Parser(l)
            print(p.parse())
        except ParserError as discrepancy:
            print('ParserError: ' + discrepancy.message)
