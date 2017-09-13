#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
parser.py

@author liesegang
"""

from elements import Variable, Application, Abstraction

class Parser(object):
    """An LL(1) parser that performs syntactic analysis on lambda calculus
    source code. An abstract syntax tree is provided if the given expression is
    valid.

    Attributes:
        lexer (Lexer): A tokenizer that's iteratively read
        token (Token): The current Token object
    """

    def __init__(self, lexer):
        self.lexer = lexer
        self.token = next(self.lexer)

    def _error(self, expected):
        """Raises a ParserError that compares an expected toke type an the
        one given by the lexer.
        """
        raise ParserError(expected, self.token.kind)

    def _advance(self):
        """Move to the next token"""
        self.token = next(self.lexer)

    def _eat(self, prediction):
        if self.token.kind == prediction:
            self._advance()
        else:
            self._error(prediction)

    def _expression(self):
        """Based on the current token, this method decides if the next
        expression is an application, abstraction, or variable
        """
        if self.token.kind == 'BOF':
            return self._application('BOF')
        elif self.token.kind == '(':
            return self._application('(')
        elif self.token.kind in ['λ', '@', '|']:
            return self._abstraction()
        elif self.token.kind == 'SYMBOL':
            return self._variable()
        else:
            return self._error('SYMBOL')

    def _application(self, begin):
        """Returns expression or application"""
        if begin =='(':
            end = ')'
        elif begin == 'BOF':
            end = 'EOF'
        else:
            raise Exception("Unown application starter")

        self._advance()
        exp = self._expression()
        while self.token.kind != end:
            exp = Application(exp, self._expression())
        self._eat(end)
        return exp

    def _variable(self):
        """Returns an instance of Variable if the current token is a symbol"""
        if self.token.kind == 'SYMBOL':
            name = self.token.value
            self._advance()
            return Variable(name)
        else:
            self._error('SYMBOL')

    def _abstraction(self):
        """Returns an instance of Abstraction if the next series of tokens
        fits the form of a lambda calculus function"""
        if self.token.kind in ['λ', '@', '|']:
            self._advance()
            variable = self._variable()
            self._eat('.')
            return Abstraction(variable, self._expression())
        else:
            self._error(" or ".join(['λ', '@', '|']))

    def parse(self):
        """Returns an abstract syntax tree if the source correctly fits the
        rules of lambda calculus
        """
        return self._expression()


class ParserError(Exception):
    """Indicates a discrepancy between what a parser expexts and an actual
    value.

    Attributes:
        expected (str): The type that should have existed
        foud (str): The actual type discovered
    """

    def __init___(self, expected, found):
        message = "Expected: {}, Found: {}".format(expected, found)
        super(ParserError, self).__init__(message)
        self.expected = expected
        self.found = found
